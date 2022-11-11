"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from invoicemgmt.views import *
from invmgmt.views import list_stock, add_item, delete_stock, update_items
from clientmgmt.views import list_client, add_client, delete_client
from django.urls import include


urlpatterns = [
    #invoice app
    path('admin/', admin.site.urls),
	path('', home, name='home'),
    path('create_invoice/', create_invoice, name='create_invoice'),
    path('list_invoice/', list_invoice, name='list_invoice'),
    path('delete_invoice/<str:pk>/', delete_invoice, name="delete_invoice"),

    #inv app
    path('list_stock/',list_stock, name='list_stock'),
    path('add_item/', add_item, name='add_item'),
    path('delete_stock/<str:pk>/', delete_stock, name="delete_stock"),
    path('update_items/<str:pk>/', update_items, name="update_items"),

    #account
    path('accounts/', include('registration.backends.default.urls')),

    #client app
    path('list_client/', list_client, name='list_client'),
    path('add_client/', add_client, name='add_client'),
    path('delete_client/<str:pk>',delete_client, name='delete_client'),
]
