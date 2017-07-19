from django.contrib import admin

# Register your models here.
from .models import Post

##注册模型
admin.site.register(Post)