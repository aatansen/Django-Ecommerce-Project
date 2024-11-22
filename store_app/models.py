from django.db import models
import datetime
import os
from django.utils.text import slugify

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
