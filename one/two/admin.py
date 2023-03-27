from django.contrib import admin

from two.models import Category, Blog

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title','time_create','photo','is_published')
    list_display_links= ('id','title')
    search_fields= ('title','context')
    list_editable= ('is_published',)
    list_filter= ('is_published', 'time_create')



class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links= ('id','name')
    search_fields= ('id','name')


admin.site.register(Blog,BlogAdmin)
admin.site.register(Category,CategoryAdmin)
