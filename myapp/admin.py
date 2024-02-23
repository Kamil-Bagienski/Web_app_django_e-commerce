from django.contrib import admin
from django.urls import path
from .models import Product, Order, Customer, Payment
from .views import customer_sales_stats  
from django.contrib.admin import AdminSite



class MyAdminSite(AdminSite):
    site_header = 'Panel Administracyjny'
    index_template = 'admin/custom_admin_template.html'
    index_title = "Kamil Bagieński"

my_admin_site = MyAdminSite(name='myadmin')

my_admin_site.register(Customer)
my_admin_site.register(Product)
my_admin_site.register(Order)
my_admin_site.register(Payment)


