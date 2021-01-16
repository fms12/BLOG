from django.contrib import admin
from .models import  Post, Category, Profile, blogComment

#  here we register the models that should want in the admin page for the website
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Profile)
admin.site.register(blogComment)