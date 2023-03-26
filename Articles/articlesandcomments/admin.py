from django.contrib import admin
from .models import *
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'text', 'art')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'text')

admin.site.register(Comment, CommentAdmin)

class CommentAdminInLine(admin.TabularInline):
    model = Comment
    fk_name = 'art'
    extra = 3
@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    inlines = [CommentAdminInLine]
    prepopulated_fields = {"slug": ("title",)}


