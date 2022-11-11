from django.contrib import admin
from .models import Invoice
from .forms import InvoiceForm

# Register your models here.
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'invoice_number']
    form = InvoiceForm
    list_filter = ['name']
    search_fields = ['name']

admin.site.register(Invoice,InvoiceAdmin)