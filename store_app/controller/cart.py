from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from store_app.models import *

def add_to_cart(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            product_check=Product_Model.objects.get(id=prod_id)
            if product_check:
                if Cart_Model.objects.filter(user=request.user,product_id=prod_id).exists():
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

@login_required(login_url='login_page')
def cart_view(request):
    cart=Cart_Model.objects.filter(user=request.user)
    context={
        'cart':cart,
    }
    return render(request,'store/cart.html',context)

def update_cart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        prod_qty = int(request.POST.get('product_qty'))
        
        # Check if the product exists in the cart for the user
        if Cart_Model.objects.filter(user=request.user, product_id=prod_id).exists():
            cart = Cart_Model.objects.get(product_id=prod_id, user=request.user)
            product = Product_Model.objects.get(id=prod_id)
            
            # Check if the requested quantity is available
            if product.quantity >= prod_qty:
                cart.product_qty = prod_qty
                cart.save()
                return JsonResponse({'status': "Updated Successfully"})
            else:
                return JsonResponse({'status': f"Sorry, only {product.quantity} units are available"})

        return JsonResponse({'status': "Product not found in cart"})
    
    return redirect('index')

def delete_cart_item(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            cart_check=Cart_Model.objects.filter(user=request.user,product_id=prod_id).exists()
            if cart_check:
                cart_item=Cart_Model.objects.get(user=request.user,product_id=prod_id)
                cart_item.delete()
                return JsonResponse({'status': "Item removed successfully"})
        else:
            return JsonResponse({'status': "Login to continue"})
    return redirect('index')
