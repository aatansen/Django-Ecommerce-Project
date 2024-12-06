from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from store_app.models import *
import uuid
from django.contrib import messages

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

@login_required(login_url='login_page')
def place_order(request):
    if request.method=="POST":
        new_order = Order_Model()
        new_order.user = request.user
        new_order.fname = request.POST.get('fname')
        new_order.lname = request.POST.get('lname')
        new_order.email = request.POST.get('email')
        new_order.phone = request.POST.get('phone')
        new_order.address = request.POST.get('address')
        new_order.city = request.POST.get('city')
        new_order.state = request.POST.get('state')
        new_order.country = request.POST.get('country')
        new_order.pin_code = request.POST.get('pin_code')

        new_order.payment_mode = request.POST.get('payment_mode')
        
        cart = Cart_Model.objects.filter(user=request.user)
        cart_total_price=0
        for item in cart:
            cart_total_price=cart_total_price+item.product.selling_price*item.product_qty
        new_order.total_price = cart_total_price
        
        new_order.tracking_no = str(uuid.uuid4())
        new_order.save()
        
        new_order_items=Cart_Model.objects.filter(user=request.user)
        for item in new_order_items:
            Order_Item_Model.objects.create(
                order=new_order,
                product=item.product,
                price=item.product.selling_price,
                quantity=item.product_qty,
            )
            
            # To decrease the product quantity from available stock
            order_product = Product_Model.objects.filter(id=item.product_id).first()
            order_product.quantity=order_product.quantity - item.product_qty
            order_product.save()
            
        # clear user cart
        Cart_Model.objects.filter(user=request.user).delete()
        messages.success(request,'Your order has been place successfully')

    return redirect('/')
