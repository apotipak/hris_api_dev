from django.db import models

# Create your models here.
class Company(models.Model):
    com_id = models.DecimalField(primary_key=True, max_digits=2, decimal_places=0)
    com_sht_th = models.CharField(max_length=25, blank=True, null=True)
    com_name_th = models.CharField(max_length=200, blank=True, null=True)
    com_add1_th = models.CharField(max_length=200, blank=True, null=True)
    com_add2_th = models.CharField(max_length=200, blank=True, null=True)
    
    com_sht_en = models.CharField(max_length=25, blank=True, null=True)
    com_name_en = models.CharField(max_length=20, blank=True, null=True)
    com_add1_en = models.CharField(max_length=200, blank=True, null=True)
    com_add2_en = models.CharField(max_length=200, blank=True, null=True)
        
    com_tambol = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    com_district = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    com_city = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    com_country = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    com_zip = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)

    com_tel1 = models.CharField(max_length=50, blank=True, null=True)
    com_tel2 = models.CharField(max_length=50, blank=True, null=True)
    com_fax1 = models.CharField(max_length=50, blank=True, null=True)
    com_fax2 = models.CharField(max_length=50, blank=True, null=True)
    com_email = models.CharField(max_length=100, blank=True, null=True)

    com_taxid = models.CharField(max_length=25, blank=True, null=True)
    com_socid = models.DecimalField(max_digits=25, decimal_places=0, blank=True, null=True)
    com_brnid = models.DecimalField(max_digits=25, decimal_places=0, blank=True, null=True)
    com_soc_no = models.CharField(max_length=25, blank=True, null=True)
    com_soc_brn = models.CharField(max_length=25, blank=True, null=True)
    com_active = models.BooleanField(blank=True, null=True)
    com_main = models.SmallIntegerField(blank=True, null=True)
    com_parent = models.SmallIntegerField(blank=True, null=True)
    com_hr_month = models.SmallIntegerField(blank=True, null=True)
    com_hr_day = models.SmallIntegerField(blank=True, null=True)
    com_md = models.CharField(max_length=25, blank=True, null=True)
    com_admin = models.CharField(max_length=25, blank=True, null=True)
    com_hr = models.CharField(max_length=25, blank=True, null=True)
    com_acno = models.CharField(max_length=25, blank=True, null=True)
    
    upd_date = models.DateTimeField(blank=True, null=True)
    upd_by = models.CharField(max_length=20, blank=True, null=True)
    upd_flag = models.CharField(max_length=1, blank=True, null=True)

    signature_md_url = models.CharField(max_length=100, blank=True, null=True)
    signature_hr_url = models.CharField(max_length=100, blank=True, null=True)
    signature_admin_url = models.CharField(max_length=100, blank=True, null=True)

    created_date = models.DateTimeField(blank=True, null=True)
    created_by = models.CharField(max_length=10, blank=True, null=True)


    class Meta:
        managed: False
        db_table = "m_company"

        permissions = [
            ("import_company", "Can import company"),
            ("export_company", "Can export company"),
            ("print_company", "Can print company"),
        ]
