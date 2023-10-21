from django.contrib import admin
from .models import User
from .models import Reservation
from .models import Employee

#register models
class UserAdmin(admin.ModelAdmin):
    list_display = ('UserFirstName', 'UserLastName', 'Email', 'State')
    list_filter = ('State',)


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('ReservationID', 'TimeOfReservation', 'Date', 'UserID')
    list_filter = ('Date', 'TimeOfReservation')

admin.site.register(User)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Employee)