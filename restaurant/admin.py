from django.contrib import admin
from .models import User
from .models import Reservation
from .models import FoodMenu
from .models import Payment
from .models import Table
from .models import Order

# register models


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('ReservationID', 'TimeOfReservation', 'Date', 'UserID')
    list_filter = ('Date', 'TimeOfReservation')



admin.site.register(Reservation, ReservationAdmin)
admin.site.register(FoodMenu)
admin.site.register(Payment)
admin.site.register(Table)
admin.site.register(Order)
