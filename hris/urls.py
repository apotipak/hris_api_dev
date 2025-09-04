import os
from django.contrib import admin
from django.urls import re_path, path, include
from django.http import FileResponse
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response

from django.conf.urls.static import static

# Simple JWT
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Protected File
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.static import serve

# User API
from user.api import api as user_api_v1

# Company API
# from company.api import api as company_api_v1

# Custom Label on Django Admin Page
admin.site.site_header = "HRIS"
admin.site.site_title = "HRIS"
admin.site.index_title = "Welcome to HRIS"

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

# API - User
urlpatterns += [
    path("api/v1/", user_api_v1.urls),
]

# API - Company
# urlpatterns += [path("api/v1/company/", company_api_v1.urls)]






# Media Folder
class MediaAuthChecker(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        file_path = request.get_full_path()[1:]
        folders = file_path.split("/")[1:]
        
        print(file_path)
        print(folders[3])

        file_name = folders[3]
        media_root = os.path.join(settings.MEDIA_ROOT)
        file_path = f'{media_root}/protected/upload/users/{file_name}'

        if os.path.exists(file_path):        
            # Add additional permission checks here if needed, e.g.,
            # if not request.user.can_access_file(filename):
            #     return Response(status=403)
            return FileResponse(open(file_path, 'rb'))
        
        return Response(status=404)

if settings.DEBUG:
    print("DEBUG")
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [re_path(r'^media/(?:.*)$', MediaAuthChecker.as_view())]
else:
    urlpatterns += [re_path(r'^media/(?:.*)$', MediaAuthChecker.as_view())]


# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
