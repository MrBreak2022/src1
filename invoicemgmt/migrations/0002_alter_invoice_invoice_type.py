# Generated by Django 4.1.1 on 2022-10-18 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicemgmt', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='invoice_type',
            field=models.CharField(blank=True, choices=[('Receipt', 'Receipt'), ('Invoice', 'Invoice')], default='', max_length=50, null=True),
        ),
    ]