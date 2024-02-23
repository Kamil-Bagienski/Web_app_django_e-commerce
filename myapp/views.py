# myapp/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Max, Min, Sum, Count
from .models import Order, Product, Customer
from django.utils.timezone import make_aware
from datetime import datetime
from django.db.models.functions import TruncDay
from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def get_products():
    products = Product.objects.all().values('id', 'name', 'price')
    return products

def index(request):
    products = get_products()
    return render(request, 'index.html', {'products': products})

def add_customer(name, email):
    pass

def add_customer_route(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        add_customer(name, email)

    return redirect('index')

def add_order(customer_id, product_id, quantity):
    try:
        order = Order.objects.create(customer_id=customer_id, product_id=product_id, quantity=quantity)
    except Exception as e:
        print(f"Błąd zamówienia: {e}")

def add_order_route(request):
    if request.method == 'POST':
        customer_id = int(request.POST.get('customer_id'))
        product_id = int(request.POST.get('product_id'))
        quantity = int(request.POST.get('quantity'))

        print("Dane formularza:", customer_id, product_id, quantity)  # Dodane do debugowania

        try:
            order = Order.objects.create(customer_id=customer_id, product_id=product_id, quantity=quantity)
            order_id = order.id 
            success_message = f"Zamówienie nr {order_id} zostało dodane pomyślnie."
            print("Zamówienie utworzone:", order_id)  # Dodane do debugowania
        except Exception as e:
            print(f"Błąd przy tworzeniu zamówienia: {e}")  # Dodane do debugowania
            success_message = None

        products = get_products()
        context = {'products': products, 'success_message': success_message}
        print("Kontekst wysyłany do szablonu:", context)  # Dodane do debugowania

        return render(request, 'index.html', context)
    print("Nie znaleziono danych formularza")  # Dodane do debugowania

    return redirect('index')

def add_payment(order_id, amount):
    pass

@login_required
def customer_sales_stats(request):
    total_sales_per_customer = Order.objects.values('customer__name').annotate(total_spent=Sum('amount'))
    
    total_products_per_customer = Order.objects.values('customer__name').annotate(total_products=Count('id'))

    return render(request, 'sales_stats.html', {'sales': total_sales_per_customer, 'products': total_products_per_customer})

def product_list(request):
    products = Product.objects.all().values('id', 'name')
    return JsonResponse(list(products), safe=False)

def product_sales_stats(request):
    product_id = request.GET.get('product_id')
    if not product_id:
        return JsonResponse({'error': 'Brak podanego ID produktu'}, status=400)

    sales_data = (
        Order.objects.filter(product_id=product_id)
        .values('order_date')
        .annotate(total_quantity=Sum('quantity'))
        .order_by('order_date')
    )

    return JsonResponse(list(sales_data), safe=False)
@login_required
def sales_in_date_range(request):
    start_date = request.GET.get('startDate')
    end_date = request.GET.get('endDate')
    
    if not start_date or not end_date:
        return JsonResponse({'error': 'Nie podano daty początkowej lub końcowej'}, status=400)
    
    start_date_aware = make_aware(datetime.strptime(start_date, '%Y-%m-%d'))
    end_date_aware = make_aware(datetime.strptime(end_date, '%Y-%m-%d'))

    sales_data = Order.objects.filter(order_date__range=[start_date_aware, end_date_aware]).values(
        'customer__id', 
        'customer__name',
        'product__name'
    ).annotate(total_quantity=Sum('quantity')).order_by('customer')
    
    return JsonResponse(list(sales_data), safe=False)

@login_required
def customer_expenses_stats(request):
    customer_id = request.GET.get('customer_id')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if customer_id:
        query = Order.objects.filter(customer_id=customer_id)
        if start_date:
            query = query.filter(order_date__gte=start_date)
        if end_date:
            query = query.filter(order_date__lte=end_date)

        data = list(query.values('order_date')
                    .annotate(total_amount=Sum('amount'))
                    .order_by('order_date'))
        return JsonResponse(data, safe=False)

    return JsonResponse({'error': 'No customer ID provided'}, status=400)

@login_required
def payment_method_stats(request):
    payment_method_id = request.GET.get('payment_method_id')
    start_date_str = request.GET.get('start_date')
    end_date_str = request.GET.get('end_date')

    if not all([payment_method_id, start_date_str, end_date_str]):
        return JsonResponse({'error': 'Brak wymaganych parametrów'}, status=400)
    
    start_date_naive = datetime.strptime(start_date_str, '%Y-%m-%d')
    end_date_naive = datetime.strptime(end_date_str, '%Y-%m-%d')
    
    end_date_naive = end_date_naive.replace(hour=23, minute=59, second=59)
    
    start_date_aware = timezone.make_aware(start_date_naive, timezone.get_default_timezone())
    end_date_aware = timezone.make_aware(end_date_naive, timezone.get_default_timezone())

    data = (
        Order.objects.filter(payment_method=payment_method_id, order_date__range=[start_date_aware, end_date_aware])
        .annotate(date=TruncDay('order_date'))
        .values('date')
        .annotate(total_amount=Sum('amount'))
        .order_by('date')
    )

    response_data = list(data)
    return JsonResponse(response_data, safe=False)

def customer_list(request):
    customers = list(Customer.objects.values('id', 'name'))
    return JsonResponse(customers, safe=False)

def your_payment_methods_view(request):
    payment_methods = Order.PAYMENT_METHODS
    formatted_methods = [{"id": method[0], "name": method[1]} for method in payment_methods]
    return JsonResponse(formatted_methods, safe=False)

@login_required
def product_sales_stats_view(request):
    return render(request, 'product_sales_stats.html')

@login_required
def sales_data_table_view(request):
    return render(request, 'sales_data_table.html')

@login_required
def customer_expenses(request):
    return render(request, 'customer_expenses_stats.html')

@login_required
def payment_method_stats_page(request):
    return render(request, 'payment_method_expenses_stats.html')

def add_payment_route(request):
    if request.method == 'POST':
        order_id = int(request.POST.get('order_id'))
        amount = float(request.POST.get('amount'))
        add_payment(order_id, amount)

    return redirect('index')

def create_order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 0))
        payment_method = request.POST.get('payment_method')

        customer, created = Customer.objects.get_or_create(name=name, email=email)

        product = get_object_or_404(Product, id=product_id)

        total_amount = product.price * quantity

        order = Order.objects.create(
            customer=customer,
            product=product,
            quantity=quantity,
            payment_method=payment_method,
            amount=total_amount
        )
        messages.success(request, "Zamówienie zostało dodane pomyślnie.")

        print(f"Zamówienie nr {order.id} zostało utworzone")
        return redirect('index')

    return redirect('index')
