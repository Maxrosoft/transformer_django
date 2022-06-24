from django.contrib import admin
from .models import Post, MainData, AboutUsData


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'publish')
    list_filter = ('created', 'publish')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish'
    ordering = ['publish']


@admin.register(MainData)
class MainDataAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']


@admin.register(AboutUsData)
class AboutUsDataAdmin(admin.ModelAdmin):
    list_display = ('adds', 'contacts')
    search_fields = ('adds', 'contacts')