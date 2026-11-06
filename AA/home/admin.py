from django.contrib import admin
from .models import Post

@admin.register(Post)
class postAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'user', 'created_at']
    list_filter = ['user', 'is_published']
    search_fields = ['title', 'body']
    ordering = ('-created_at',)
    prepopulated_fields = {'slug': ('title',)}