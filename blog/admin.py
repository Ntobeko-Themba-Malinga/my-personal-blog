from django.contrib import admin
from .models import Post, Subscriber, Project


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'created']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = { 'slug': ('title',) }


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['thumbnail', 'title', 'author', 'status']
    list_filter = ['author']
    search_fields = ['title', 'body']
    prepopulated_fields = { 'slug': ('title',) }
