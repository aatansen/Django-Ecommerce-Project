from django.shortcuts import render,redirect
from django.http import JsonResponse
from store_app.models import *

def add_to_cart(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            product_check=Product_Model.objects.get(id=prod_id)
            if product_check:
                if Cart_Model.objects.filter(user=request.user,product_id=prod_id):
                    return JsonResponse({'status':"Product already in cart"})
                else:
                    prod_qty=int(request.POST.get('product_qty'))
                    if product_check.quantity>=prod_qty:
                        Cart_Model.objects.create(user=request.user,product_id=prod_id,product_qty=prod_qty)
                        return JsonResponse({'status':"Product added successfully"})
                    else:
                        return JsonResponse({'status':f"Only {product_check.quantity} item is available"})
            else:
                return JsonResponse({'status':"No such product found"})
        else:
            return JsonResponse({'status':"Login to Continue"})
    
    return redirect('index')

def cart_view(request):
    cart=Cart_Model.objects.filter(user=request.user)
    context={
        'cart':cart,
    }
    return render(request,'store/cart.html',context)