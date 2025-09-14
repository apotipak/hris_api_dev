from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):

    class Meta:
        managed = False
        db_table = 'employee'
        default_permissions = []

        permissions = [
            ("m1_employee_create", "Can create M1"),
            ("m1_employee_read", "Can read M1"),
            ("m1_employee_update", "Can update M1"),
            ("m1_employee_delete", "Can delete M1"),
            ("m1_employee_import", "Can import M1"),
            ("m1_employee_export", "Can export M1"),
            ("m1_employee_see_salary", "Can see M1 salary"),
            ("m1_employee_update_salary", "Can update M1 salary"),
        ]


