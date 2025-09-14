from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):

    class Meta:
        managed = False
        db_table = 'employee'
        default_permissions = []

        permissions = [
            ("d3_employee_create", "Can create D3"),
            ("d3_employee_read", "Can read D3"),
            ("d3_employee_update", "Can update D3"),
            ("d3_employee_delete", "Can delete D3"),
            ("d3_employee_import", "Can import D3"),
            ("d3_employee_export", "Can export D3"),
            ("d3_employee_see_salary", "Can see D3 salary"),
            ("d3_employee_update_salary", "Can update D3 salary"),
        ]


