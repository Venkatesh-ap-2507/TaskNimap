from django.contrib import admin
from .models import User, Client, Project

class Useradmin(admin.ModelAdmin):
    list_display = ("id", 'name')

class Clientadmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'created_at', 'created_by')

class Projectadmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'client', 'get_users', 'created_at', 'created_by')

    def get_users(self, obj):
        return ", ".join([user.name for user in obj.users.all()])

    get_users.short_description = 'Users'

admin.site.register(User, Useradmin)
admin.site.register(Client, Clientadmin)
admin.site.register(Project, Projectadmin)
