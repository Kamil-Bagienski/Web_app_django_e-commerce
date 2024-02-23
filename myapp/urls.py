# myappurls.py
from django.urls import path, include
from .views import index, add_order_route, create_order, customer_sales_stats, product_sales_stats_view, product_list,product_sales_stats, sales_in_date_range, sales_data_table_view
from .views import payment_method_stats_page, your_payment_methods_view, payment_method_stats
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', index, name='index'),
    path('create_order', create_order, name='create_order'),
    path('add_order', add_order_route, name='add_order'),
    path('sales_stats/', customer_sales_stats, name='sales_stats'), 
    path('api/products/', product_list, name='product-list'),
    path('api/product-sales-stats/', product_sales_stats, name='product-sales-stats'),
    path('product-sales-stats/', product_sales_stats_view, name='product-sales-stats-view'),
    path('api/sales-in-date-range/', sales_in_date_range, name='sales-in-date-range'),
    path('sales-data-table/', sales_data_table_view, name='sales-data-table'),
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('api/customer-expenses-stats/', views.customer_expenses_stats, name='customer_expenses_stats'),
    path('api/customers/', views.customer_list, name='customer_list'),
    path('customer-expenses/', views.customer_expenses, name='customer_expenses'),
    path('api/payment-method-stats/', payment_method_stats, name='payment-method-stats'),
    path('payment-method-stats/', payment_method_stats_page, name='payment-method-stats-page'),
    path('api/payment-methods/', your_payment_methods_view, name='payment-methods'),
]