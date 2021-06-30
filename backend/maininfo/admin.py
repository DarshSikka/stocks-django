from django.contrib import admin
from .models import CompanyStock
# Register your models here.

class CompanyStockAdmin(admin.ModelAdmin):
    list_display=('company_name', 'company_stocks_as_comma_seperated_numbers')
admin.site.register(CompanyStock, CompanyStockAdmin)