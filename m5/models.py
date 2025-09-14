from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):

    class Meta:
        managed = False
        db_table = 'employee'
        default_permissions = []

        permissions = [
            ("m5_employee_create", "Can create M5"),
            ("m5_employee_read", "Can read M5"),
            ("m5_employee_update", "Can update M5"),
            ("m5_employee_delete", "Can delete M5"),
            ("m5_employee_import", "Can import M5"),
            ("m5_employee_export", "Can export M5"),
            ("m5_employee_see_salary", "Can see M5 salary"),
            ("m5_employee_update_salary", "Can update M5 salary"),
        ]


