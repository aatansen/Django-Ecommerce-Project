from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from store_app.models import *

@login_required(login_url='login_page')
def wishlist_view(request):
    wishlist=Wishlist_Model.objects.filter(user=request.user)
    context={
        'wishlist':wishlist,
    }
    return render(request,'store/wishlist.html',context)

def add_to_wishlist(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            product_check=Product_Model.objects.get(id=prod_id)
            if product_check:
                wish_item=Wishlist_Model.objects.filter(user=request.user,product_id=prod_id)
                if wish_item.exists():
                    return JsonResponse({'status': "Item already in wishlist"})
                else:
                    wish=Wishlist_Model.objects.create(user=request.user,product_id=prod_id)
                    wish.save()
                    return JsonResponse({'status': "Item Added to wishlist"})
            else:
                return JsonResponse({'status': "No such product found"})
                
    return redirect('index')

def delete_wishlist_item(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            prod_id=int(request.POST.get('product_id'))
            wishlist_check=Wishlist_Model.objects.filter(user=request.user,product_id=prod_id)
            if wishlist_check:
                wishlist_item=Wishlist_Model.objects.get(user=request.user,product_id=prod_id)
                wishlist_item.delete()
                return JsonResponse({'status': "Product removed from wishlist"})
            else:
                return JsonResponse({'status': "Product not found in wishlist"})
        else:
            return JsonResponse({'status': "Login to continue"})
    return redirect('index')