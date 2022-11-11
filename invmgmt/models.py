from django.db import models

# Create your models here.
class Stock(models.Model):
	category = models.CharField("Category:", max_length=50, default='', blank=True, null=True)
	item_name = models.CharField("Item Name:", max_length=50, blank=True, null=True)
	quantity = models.IntegerField("Quantity:", default='0', blank=True, null=True)
	set_price = models.CharField ("Pricing:", max_length=50, default='', blank=True, null=True)
	receive_quantity = models.IntegerField(default='0', blank=True, null=True)
	receive_by = models.CharField(max_length=50, blank=True, null=True)
	issue_quantity = models.IntegerField(default='0', blank=True, null=True)
	issue_by = models.CharField(max_length=50, blank=True, null=True)
	issue_to = models.CharField(max_length=50, blank=True, null=True)
	phone_number = models.CharField(max_length=50, blank=True, null=True)
	created_by = models.CharField(max_length=50, blank=True, null=True)

	def __str__(self):
		return self.category