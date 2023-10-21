from django.db import models

# restaurant/models.py
from django.db import models

class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    UserFirstName = models.CharField(max_length=50)
    UserLastName = models.CharField(max_length=50)
    UserName = models.CharField(max_length=50)
    Password = models.CharField(max_length=100)
    Email = models.EmailField()
    DOB = models.DateField()
    Address1 = models.CharField(max_length=100)
    Address2 = models.CharField(max_length=100, blank=True, null=True)
    City = models.CharField(max_length=50)
    State = models.CharField(
        max_length=2,
        choices=[
            ('NE', 'Nebraska'),
            ('IA', 'Iowa'),
            # Add the remaining states here, if we have time...
        ]
    )
    ZipCode = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.UserFirstName} {self.UserLastName}"


class Reservation(models.Model):
    ReservationID = models.AutoField(primary_key=True)
    TimeOfReservation = models.TimeField(
        choices=[
            ('11:00:00', '11:00 AM'),
            ('11:15:00', '11:15 AM'),
            ('11:30:00', '11:30 AM'),
            ('11:45:00', '11:45 AM'),
            ('12:00:00', '12:00 PM'),
            ('12:15:00', '12:15 PM'),
            ('12:30:00', '12:30 PM'),
            ('12:45:00', '12:45 PM'),
            ('13:00:00', '01:00 PM'),
            ('13:15:00', '01:15 PM'),
            ('13:30:00', '01:30 PM'),
            ('13:45:00', '01:45 PM'),
            ('14:00:00', '02:00 PM'),
            ('14:15:00', '02:15 PM'),
            ('14:30:00', '02:30 PM'),
            ('14:45:00', '02:45 PM'),
            ('15:00:00', '03:00 PM'),
            ('15:15:00', '03:15 PM'),
            ('15:30:00', '03:30 PM'),
            ('15:45:00', '03:45 PM'),
            ('16:00:00', '04:00 PM'),
            ('16:15:00', '04:15 PM'),
            ('16:30:00', '04:30 PM'),
            ('16:45:00', '04:45 PM'),
            ('17:00:00', '05:00 PM'),
            ('17:15:00', '05:15 PM'),
            ('17:30:00', '05:30 PM'),
            ('17:45:00', '05:45 PM'),
            ('18:00:00', '06:00 PM'),
            ('18:15:00', '06:15 PM'),
            ('18:30:00', '06:30 PM'),
            ('18:45:00', '06:45 PM'),
            ('19:00:00', '07:00 PM'),
            ('19:15:00', '07:15 PM'),
            ('19:30:00', '07:30 PM'),
            ('19:45:00', '07:45 PM'),
            ('20:00:00', '08:00 PM'),
            ('20:15:00', '08:15 PM'),
            ('20:30:00', '08:30 PM'),
            ('20:45:00', '08:045 PM'),
            ('21:00:00', '09:00 PM'),
        ]
    )
    Date = models.DateField()
    UserID = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')

    def __str__(self):
        return f"Reservation for {self.UserID.UserFirstName} {self.UserID.UserLastName} on {self.Date} at {self.TimeOfReservation}"