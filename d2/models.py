from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):

    class Meta:
        managed = False
        db_table = 'employee'
        default_permissions = []

        permissions = [
            ("d2_employee_create", "Can create D2"),
            ("d2_employee_read", "Can read D2"),
            ("d2_employee_update", "Can update D2"),
            ("d2_employee_delete", "Can delete D2"),
            ("d2_employee_import", "Can import D2"),
            ("d2_employee_export", "Can export D2"),
            ("d2_employee_see_salary", "Can see D2 salary"),
            ("d2_employee_update_salary", "Can update D2 salary"),
        ]


