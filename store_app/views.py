from django.shortcuts import render
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