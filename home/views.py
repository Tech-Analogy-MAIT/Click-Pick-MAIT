from django.shortcuts import render, HttpResponse
from home.models import Order
from django.contrib import messages
from .models import Order
from django.views.decorators.csrf import csrf_exempt,csrf_protect

# Create your views here.
def index(request):
    return render(request,'index.html')

@csrf_exempt
def order(request) :
    if request.method == "POST" :
        order_name = request.POST.get('order')
        price = request.POST.get('price')
        order = Order(order_name=order_name, order_price=price)
        order.save()
        messages.success(request,'Thank You! Your order has been placed.')
    return render(request, 'order.html')