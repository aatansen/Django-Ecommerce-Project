from django.db import models
import datetime
import os
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
def get_file_path(request, filename):
    original_filename = filename
    now_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    new_filename = f"{now_time}_{original_filename}"  # Concatenate timestamp with the original filename
    return os.path.join('uploads', new_filename)  # Join directory and filename

class Category_Model(models.Model):
    slug = models.CharField(max_length=150, null=True, blank=True)  # Allow null/blank for auto-generation
    name = models.CharField(max_length=150, unique=True, null=False, blank=False)
    category_image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    description = models.TextField(max_length=500, null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=default,1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default,1=Trending")
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keywords = models.CharField(max_length=150, null=False, blank=False)
    meta_description = models.TextField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:  # Only generate slug if it's not already set
            self.slug = slugify(self.name)
        super(Category_Model, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Product_Model(models.Model):
    category = models.ForeignKey(Category_Model, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, null=True, blank=True)  # Allow null/blank for auto-generation
    name = models.CharField(max_length=150, null=False, blank=False)
    product_image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    small_description = models.TextField(max_length=250, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    original_price = models.FloatField(null=False, blank=False)
    selling_price = models.FloatField(null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=default,1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default,1=Trending")
    tag = models.CharField(max_length=150, null=False, blank=False)
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keywords = models.CharField(max_length=150, null=False, blank=False)
    meta_description = models.TextField(max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it's not set
            base_slug = slugify(self.name)
            slug = base_slug
            counter = 1
            # Check if slug already exists
            while Product_Model.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super(Product_Model, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Cart_Model(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product_Model, on_delete=models.CASCADE)
    product_qty=models.IntegerField(null=False,blank=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} added {self.product_qty} unit(s) of {self.product} to their Cart"

class Wishlist_Model(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(Product_Model, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} added {self.product} to their Wishlist"

class Order_Model(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    fname=models.CharField(max_length=150,null=False)
    lname=models.CharField(max_length=150,null=False)
    email=models.CharField(max_length=150,null=False)
    phone=models.CharField(max_length=150,null=False)
    address=models.TextField(null=False)
    city=models.CharField(max_length=150,null=False)
    state=models.CharField(max_length=150,null=False)
    country=models.CharField(max_length=150,null=False)
    pin_code=models.CharField(max_length=150,null=False)
    total_price=models.FloatField(null=False)
    payment_mode=models.CharField(max_length=150,null=False)
    payment_id=models.CharField(max_length=250,null=True)
    order_statuses=(
        ('Pending','Pending'),
        ('Out For Shipping','Out For Shipping'),
        ('Completed','Completed'),
    )
    status=models.CharField(max_length=150,choices=order_statuses,default=order_statuses[0][1])
    message=models.TextField(null=True)
    tracking_no=models.CharField(max_length=150,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.id} - {self.tracking_no}"
    
class Order_Item_Model(models.Model):
    order=models.ForeignKey(Order_Model,on_delete=models.CASCADE)
    product=models.ForeignKey(Product_Model,on_delete=models.CASCADE)
    price=models.FloatField(null=False)
    quantity=models.IntegerField(null=False)
    
    def __str__(self):
        return f"{self.order.id} - {self.order.tracking_no}"

class Profile_Model(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    phone=models.CharField(max_length=150,null=False)
    address=models.TextField(null=False)
    city=models.CharField(max_length=150,null=False)
    state=models.CharField(max_length=150,null=False)
    country=models.CharField(max_length=150,null=False)
    pin_code=models.CharField(max_length=150,null=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.user.email}"