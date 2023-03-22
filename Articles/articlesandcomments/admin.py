from django.contrib import admin
from .models import *


class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')

admin.site.register(Articles, ArticlesAdmin)



class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', 'art')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'text')


admin.site.register(Comment, CommentAdmin)
