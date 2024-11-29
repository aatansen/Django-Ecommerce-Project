from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from store_app.models import *

def checkout_view(request):
    rawCart=Cart_Model.objects.filter(user=request.user)
    for item in rawCart:
        if item.product_qty>item.product.quantity:
            Cart_Model.objects.delete(id=item.id)
    cartItems=Cart_Model.objects.filter(user=request.user)
    total_price=0
    for item in cartItems:
        total_price=total_price+item.product.selling_price*item.product_qty

    context={
        'cartItems':cartItems,
        'total_price':total_price,
    }
    return render(request,'store/checkout.html',context)
