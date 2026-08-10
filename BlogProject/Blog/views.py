from django.shortcuts import render
from .models import Category,Blog

# Create your views here.

def home(request):
    catagories=Category.objects.all()
    featuredPost=Blog.objects.filter(is_featured=True,status='Published').order_by('-updated_at')
    post=Blog.objects.filter(is_featured=False,status='Published')
    context={
        'categories':catagories,
        'featuredpost':featuredPost,
        'posts':post
        }
    return render(request,'blog/home.html',context)