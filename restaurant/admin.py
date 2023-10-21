from django.contrib import admin
from .models import User

#register models
class UserAdmin(admin.ModelAdmin):
    list_display = ('UserFirstName', 'UserLastName', 'Email', 'State')
    list_filter = ('State',)

admin.site.register(User)

