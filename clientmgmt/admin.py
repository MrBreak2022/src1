from django.contrib import admin
from .models import Client
from .forms import ClientCreateForm

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = ['client_name','category','contact_number']
    form = ClientCreateForm
    list_filter = ['client_name']
    search_fields = ['client_name', 'category']

admin.site.register(Client,ClientAdmin)