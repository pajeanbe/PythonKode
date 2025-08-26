from django.contrib import admin
from .models import Topic, Article

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'topic', 'author', 'created_at')
    list_filter = ('topic', 'author', 'created_at')
    search_fields = ('title', 'content')

admin.site.register(Topic)
admin.site.register(Article, ArticleAdmin)
