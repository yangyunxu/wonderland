from django.contrib import admin
from category.models import Category, Page, Comment

# Register your models here.
admin.site.register(Category)
admin.site.register(Page)
admin.site.register(Comment)