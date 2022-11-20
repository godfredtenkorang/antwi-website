from xml.etree.ElementTree import Comment
from django.contrib import admin
from .models import *

admin.site.register(Post)
admin.site.register(Blog)
admin.site.register(BlogPost)
admin.site.register(Service)
admin.site.register(Contact)
