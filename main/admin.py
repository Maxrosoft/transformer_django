from django.contrib import admin
from .models import Post, MainData, AboutUsData, Comment


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
    list_display = ('adds', 'contacts', 'email')
    search_fields = ('adds', 'contacts', 'email')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')