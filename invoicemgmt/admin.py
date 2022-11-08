from django.contrib import admin
from .models import Invoice
from .forms import InvoiceForm

# Register your models here.
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['company_name','invoice_number','name', 'invoice_date']
    form = InvoiceForm
    list_filter = ['company_name']
    search_fields = ['name']
admin.site.register(Invoice, InvoiceAdmin)