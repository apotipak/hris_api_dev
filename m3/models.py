from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):

    class Meta:
        managed = False
        db_table = 'employee'
        default_permissions = []

        permissions = [
            ("m3_employee_create", "Can create M3"),
            ("m3_employee_read", "Can read M3"),
            ("m3_employee_update", "Can update M3"),
            ("m3_employee_delete", "Can delete M3"),
            ("m3_employee_import", "Can import M3"),
            ("m3_employee_export", "Can export M3"),
            ("m3_employee_see_salary", "Can see M3 salary"),
            ("m3_employee_update_salary", "Can update M3 salary"),
        ]


