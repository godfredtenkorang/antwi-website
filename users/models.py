from django.db import models
from folio.models import *

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    content = models.TextField()
    
    def __str__(self):
        return self.user.username