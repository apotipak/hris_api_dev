import os

from django.http import JsonResponse
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from ninja import NinjaAPI
from ninja.security import SessionAuth, HttpBearer
from ninja_extra import NinjaExtraAPI, api_controller, route, throttle, permissions
from ninja_jwt.authentication import JWTAuth
from ninja.security import django_auth
from ninja.security import HttpBearer
from django.http import HttpRequest

from django.contrib.auth.models import Permission

from hris import settings
from django.shortcuts import get_object_or_404
from django.http import FileResponse
from django.http import HttpResponse, Http404

from .models import User, UserProfile
from django.db.models import F

from django_user_agents.utils import get_user_agent

# from user.models import User



api = NinjaAPI(version='1.0', urls_namespace='main_api')


# class AuthBearer(HttpBearer):
#     def authenticate(self, request, token):
#         if token == "supersecret":
#             return token



@api.get("/hi")
def hello(request):
    return "Welcome to HRIS system"


@api.get("/device-info", auth=[SessionAuth(), JWTAuth()])
def deviceInfo(request:HttpRequest):    
    user_agent = get_user_agent(request)

    client_ip_address = "unknown"
    client_device = "unknown"
    client_os = "unknown"
    client_browser = "unknown"

    # IP Address
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        client_ip_address = x_forwarded_for.split(',')[-1].strip()
    else:
        client_ip_address = request.META.get('REMOTE_ADDR')            
    
    client_device = user_agent.os.family
    # client_os = user_agent.os.family + " (" + user_agent.os.version_string + ")"
    # client_browser = user_agent.browser.family + " (" + user_agent.browser.version_string + ")"

    # ทดสอบบน local ให้คอมเม้นท์ 2 บรรทัดนี้ 
    # ****** แต่เอาขึ้น production ต้องเอาคอมเม้นท์ออก *****
    client_os = request.user_agent.os.family + " (" + request.user_agent.os.version_string + ")"
    client_browser = request.user_agent.browser.family + " (" + request.user_agent.browser.version_string + ")"


    data = {
        'client_ip_address': client_ip_address,
        'client_device': client_device,
        'client_os': client_os,
        'client_browser': client_browser
    }
    print("device-info", data)

    return JsonResponse(data)


@api.get("/me", auth=[SessionAuth(), JWTAuth()])
@throttle
def me(request:HttpRequest):

    userid = request.user.id
    print("userid", userid)


    try:
        User = get_user_model()
        # user = list(User.objects.filter(id=userid).all().values('username', 'email', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active', 'userprofile__display_name'))
        user = list(User.objects
                    .annotate(display_name=F('userprofile__display_name'))
                    .annotate(avatar_file_name=F('userprofile__avatar_file'))
                    .filter(id=userid).all()
                    .values('username', 'email', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active', 'display_name', 'avatar_file_name')
                    )
        
        # print("user_profile", user)

        return user


    except User.DoesNotExist:
        error = JsonResponse({'error': 'User does not exist'}, status=500)
        # print("Error 1", error)
    except Exception as e:
        error = JsonResponse({'error': 'An unexpected error occurred'}, status=500)
        # print("Error 2", error)

    return None



# @api.get('/media/protected/upload/users/{file_name}/', auth=[AuthBearer(), JWTAuth()])
@api.get('/media/protected/upload/users/{file_name}/', auth=[SessionAuth(), JWTAuth()])
def get(request, file_name):

    # print("file_name", file_name)
    # print("request", request.META["REMOTE_ADDR"])

    media_root = os.path.join(settings.MEDIA_ROOT)
    file_path = f'{media_root}/protected/upload/users/{file_name}'

    if os.path.exists(file_path):        
        # Add additional permission checks here if needed, e.g.,
        # if not request.user.can_access_file(filename):
        #     return Response(status=403)
        return FileResponse(open(file_path, 'rb'))

    return Response(status=404)


@api.get('/my-permissions', auth=[SessionAuth(), JWTAuth()])
def get(request):
    
    userid = request.user.id
    permission_list = {}
    group_permission_list = {}

    # User Permissions
    user = User.objects.get(id=userid)
    

    # print("user", user)
    # print(Permission.objects.filter(group__user=user))
    print("permissions", list(user.get_all_permissions()))

    # res = list(user.user_permissions.all())
    # for item in res:
    #     print(item)


    # permission_list = list(user.user_permissions.all().values_list('codename', flat=True))
    # permission_list = list(user.user_permissions.all().values_list('name', flat=True))
    # permission_list = list(user.user_permissions.all().values_list('content_type_id__model', flat=True))
    permission_list = list(user.get_all_permissions())
    return permission_list

    '''
    # print("perm_list", perm_list)
    # for permission in permission_list:
    #     print(f"User has permission 1: {permission}")

    # User Group Permissions
    group_permission_list = list(Permission.objects.filter(group__user=user).distinct().values_list('codename', flat=True))
    # group_permission_list = list(Permission.objects.filter(group__user=user).distinct().values_list('name', flat=True))
    # group_permission_list = list(Permission.objects.filter(group__user=user).distinct().values_list('content_type_id__model', flat=True))

    # group_permissions = Permission.objects.filter(group__user=user)
    # print("group_permissons", group_permissions)
    # for permission in group_permission_list:
    #     print(f"User has permission 2: {permission}")


    # Combine All Permissions
    combined_distinct_permission_list = list(set(permission_list + group_permission_list))

    return combined_distinct_permission_list
    '''
    