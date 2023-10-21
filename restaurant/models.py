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

