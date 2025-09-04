from django.db import models

class Module(models.Model):

    class Meta:
        verbose_name = 'module'
        default_permissions = []

        permissions = [            
            # Master Data > Company
            ("master_data.menu.company.submenu.company_information", "Master Data | Can see Company Information menu"),
        ]