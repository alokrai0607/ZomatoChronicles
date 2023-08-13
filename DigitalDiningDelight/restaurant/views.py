from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Dish, Order

def menu_list(request):
    dishes = Dish.objects.all()
    return render(request, 'restaurant/menu_list.html', {'dishes': dishes})

def place_order(request):
    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        dish_ids = request.POST.getlist('dish_id')
        dishes = Dish.objects.filter(id__in=dish_ids)

        order = Order.objects.create(customer_name=customer_name)
        order.dishes.set(dishes)

        return redirect('menu-list')

    dishes = Dish.objects.all()
    return render(request, 'restaurant/place_order.html', {'dishes': dishes})

def admin_page(request):
    orders = Order.objects.all()
    return render(request, 'restaurant/admin_page.html', {'orders': orders})

