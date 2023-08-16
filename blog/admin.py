from django.contrib import admin

from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'creation_date', 'publication_attribute', 'number_of_views',)
    list_filter = ('publication_attribute',)
    search_fields = ('title',)
