from django.db import models

# Create your models here.
class Client(models.Model):
    client_name = models.CharField('Client Name:', max_length=200, default='', blank=True, null=True)
    category_choice = (
        ('Supplier', 'Supplier'),
        ('Customer', 'Customer'),
    )
    category = models.CharField('Category:', max_length=50, default='', blank=True, null=True, choices=category_choice)
    contact_number = models.IntegerField('Contact Number:', max_length='10', blank=True, null=True)

    def __str__(self):
        return self.client_name