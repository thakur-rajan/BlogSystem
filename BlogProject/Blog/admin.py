from django.contrib import admin
from .models import Category,Blog
# Register your models here.
@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display=['categoryName']
    

@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display=['title','author']
    prepopulated_fields={'slug':('title',)}
    search_fields=('id','title','author','category_categoryName','status')
    
