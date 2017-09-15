from django.contrib import admin

from .models import ResUsers

@admin.register(ResUsers)
class ResUsersModelAdmin(admin.ModelAdmin):

    list_display = ['user_name','mobile','login']
    list_filter = ['active']
    search_fields = ['user_name','login','mobile']

    class Meta:
        model = ResUsers
