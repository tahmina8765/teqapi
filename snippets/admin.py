from django.contrib import admin

# Register your models here.

from .models import Snippet

@admin.register(Snippet)
class SnippetModelAdmin(admin.ModelAdmin):

    list_display = ['id', 'title','code']
    search_fields = ['title', 'code']

    class Meta:
        model = Snippet


# admin.site.register(Snippet)