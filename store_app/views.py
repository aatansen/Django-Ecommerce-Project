from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *

# Create your views here.
def index(request):
    return render(request,'store/index.html')

def collections(request):
    category=Category_Model.objects.filter(status='0')
    
    context={
        'category':category
    }
    return render(request,'store/collections.html',context)

def collection_view(request,slug):
    cat=Category_Model.objects.filter(status='0',slug=slug)
    
    if cat:
        products=Product_Model.objects.filter(category__slug=slug)
        category=cat.first()
        
        context={
            'products':products,
            'category':category,
        }
        return render(request,'store/products/index.html',context)
    else:
        messages.warning(request,"No such category found")
        return redirect('collections')
    
def product_view(request,cat_slug,prod_slug):
    cat=Category_Model.objects.filter(slug=cat_slug,status="0")
    if cat:
        prod = Product_Model.objects.filter(slug=prod_slug,status="0")
        if prod:
            product=prod.first()
            context={
                "product":product,
            }
        else:
            messages.error(request,"No such product found")
            return redirect("collections")
    else:
        messages.error(request,"No such category found")
        return redirect("collections")
    return render(request,"store/products/view.html",context)