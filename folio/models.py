
from django.db import models
from PIL import Image
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    image = models.ImageField(upload_to="home_post_img", default="")
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title
    
    def save(self):
        super().save()
        
        img = Image.open(self.image.path)
        if img.height > 350 or img.width > 350:
            output_size = (350, 350)
            img.thumbnail(output_size)
            img.save(self.image.path)
            
class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="home_blog", default="")
    datetime = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to="blog_post", default="")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Service(models.Model):
    image1 = models.ImageField(upload_to="service_img", default="")
    image2 = models.ImageField(upload_to="service_img", default="")
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    