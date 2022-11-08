from django.contrib import admin
from .models import Stock
from .forms import StockAddForm
# Register your models here.
class StockAdmin(admin.ModelAdmin):
    list_display = ['category','item_name',]
    form = StockAddForm
    list_filter = ['category']
    search_fields = ['item_name']
admin.site.register(Stock, StockAdmin)