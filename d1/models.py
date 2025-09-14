from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):

    class Meta:
        managed = False
        db_table = 'employee'
        default_permissions = []

        permissions = [
            ("d1_employee_create", "Can create D1"),
            ("d1_employee_read", "Can read D1"),
            ("d1_employee_update", "Can update D1"),
            ("d1_employee_delete", "Can delete D1"),
            ("d1_employee_import", "Can import D1"),
            ("d1_employee_export", "Can export D1"),
            ("d1_employee_see_salary", "Can see D1 salary"),
            ("d1_employee_update_salary", "Can update D1 salary"),
        ]


