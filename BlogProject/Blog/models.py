from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    categoryName=models.CharField(max_length=50,unique=True)
    createdAt=models.DateTimeField(auto_now_add=True)
    updatedAt=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural='catgories'

    def __str__(self):
        return self.categoryName


class Blog(models.Model):
    title=models.CharField(max_length=100,null=False)
    slug=models.SlugField(max_length=150,unique=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    featuredImage=models.ImageField(upload_to='uploads/%y/%m/%d')
    shortDescription=models.TextField(max_length=500)
    blog_body = models.TextField(max_length=2000)
    
    STATUS_CHOICES = (
        ("Draft", "Draft"),
        ("Published", "Published")
    )
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Draft")
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
