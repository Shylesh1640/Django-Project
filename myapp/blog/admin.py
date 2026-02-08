from django.contrib import admin
from .models import Post, Category, AboutUs

# Register your models here.



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content')
    search_fields = ('title', 'content')
    list_filter = ('Category','created_at')

admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(AboutUs)