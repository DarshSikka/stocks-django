from django.db import models

# Create your models here.
class CompanyStock(models.Model):
    company_name=models.CharField(max_length=500)
    company_stocks_as_comma_seperated_numbers=models.TextField()