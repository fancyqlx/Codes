from django.contrib import admin
from blog.models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    exclude = ['posted']
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'posted')
    list_filter = ['category']
    search_fields = ['title']

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
