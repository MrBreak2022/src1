# Generated by Django 4.1.1 on 2022-11-09 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invmgmt', '0003_stock_set_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
