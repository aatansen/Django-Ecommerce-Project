from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from store_app.models import Order_Model,Order_Item_Model
import uuid
from django.contrib import messages
from django.contrib.auth.models import User

@login_required(login_url='login_page')
def my_orders(request):
    orders=Order_Model.objects.filter(user=request.user)
    
    context={
        "orders":orders,
    }
    return render(request,'store/orders/index.html',context)

@login_required(login_url='login_page')
def view_order(request,tr_no):
    order=Order_Model.objects.filter(tracking_no=tr_no).filter(user=request.user).first()
    orderItems=Order_Item_Model.objects.filter(order=order)
    context={
        "order":order,
        "orderItems":orderItems,
    }
    return render(request,'store/orders/view.html',context)