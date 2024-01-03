from django.contrib import admin

from petstagram.accounts.models import PetstagramUser


@admin.register(PetstagramUser)
class AdminPetstagramUser(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'gender')