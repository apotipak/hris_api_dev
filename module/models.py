from django.db import models

'''
1. Master Data (MODULE)
    1.1 Company (MENU)
        1.1.1 Company Information
        1.1.2 Company Type
        1.1.8 Zone

    1.2 Main Table (MENU)
        1.2.1 Address Type
        1.2.2 Bank
        1.2.? Wage Zone


2. Employee (MODULE)
    2.1 Employee (MENU)
        2.1.1 General
        2.1.2 Recommend
        2.1.? Documents

3. Income / Deduct (MODULE)
    3.1 Income / Deduct
        3.1.1 Income / Deduct Maintenance
        3.1.2 TPA / TPB Maintenance
        3.1.3 Import Uniform (not use)


'''

class Module(models.Model):

    class Meta:
        verbose_name = 'module'
        default_permissions = []

        permissions = [            
            # 1. Master Data > 1.1 Company
            ("master_data.menu.company.submenu.company_information", "Master Data | Can see Company Information menu"), # 1.1.1
            ("master_data.menu.company.submenu.company_type", "Master Data | Can see Company Type menu"), # 1.1.2
            ("master_data.menu.company.submenu.department", "Master Data | Can see Department menu"), # 1.1.3
            ("master_data.menu.company.submenu.division", "Master Data | Can see Division menu"),  # 1.1.4
            ("master_data.menu.company.submenu.employee_grade", "Master Data | Can see Employee Grade menu"),  # 1.1.5
            ("master_data.menu.company.submenu.position", "Master Data | Can see Position menu"), # 1.1.6
            ("master_data.menu.company.submenu.rank", "Master Data | Can see Rank menu"), # 1.1.7
            ("master_data.menu.company.submenu.section", "Master Data | Can see Section menu"), # 1.1.8
            ("master_data.menu.company.submenu.zone", "Master Data | Can see Zone menu"), # 1.1.9

            # 1. Master Data > 1.2 Main Table 
            ("master_data.menu.main_table.submenu.address_type", "Master Data | Can see Address Type menu"), # 1.2.1 Address Type
            ("master_data.menu.main_table.submenu.bank", "Master Data | Can see bank menu"), # 1.2.2 Bank


            # 2. Employee > 2.1 Employee
            ("employee.menu.employee.submenu.employee_list", "Employee | Can see Employee List menu"), 
            ("employee.menu.employee.submenu.general", "Employee | Can see General menu"), # 2.1.1 General
            ("employee.menu.employee.submenu.recommend", "Employee | Can see Recommend menu"), # 2.1.2 Recommend

            # 3. Income / Deduct
            ("income_deduct.menu.income_deduct.submenu.income_deduct_maintenance", "Income Deduct | Can see Income/Deduct Maintenance menu"), 
            ("income_deduct.menu.income_deduct.submenu.tpa_tpb_maintenance", "Income Deduct | Can see TPA/TPB Maintenance menu"),          

            # 4. Payroll
            ("payroll.menu.payroll.submenu.payroll_system", "Payroll | Can see Payroll System menu"),
            ("payroll.menu.payroll.submenu.close_payment_period", "Payroll | Can see Payroll Close Payment Period menu"),

            # 5. Daily Monitoring
            ("daily_monitoring.menu.daily_monitoring.submenu.home", "Daily Monitoring | Can see Daily Monitoring Home menu"),
            
            # 6. Customer
            ("customer.menu.customer.submenu.home", "Customer | Can see Customer Home menu"),

            # 7. Contract
            ("contract.menu.contract.submenu.home", "Contract | Can see Contract Home menu"),

            # 8. Training
            ("training.menu.training.submenu.home", "Training | Can see Training Home menu"),

            # 9. License
            ("license.menu.license.submenu.home", "License | Can see License Home menu"),

            # 10. Aviation
            ("aviation.menu.aviation.submenu.home", "Aviation | Can see Aviation Home menu"),

        ]
