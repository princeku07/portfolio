from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Contact)

admin.site.register(Category)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on','categories')
    list_filter = ("status",'categories')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(Post, PostAdmin)
admin.site.register(PostComments)
