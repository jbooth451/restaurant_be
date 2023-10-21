# restaurant/models.py
from django.db import models
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError


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


class Table(models.Model):
    tableSize_choices = [
        (2, 'Table for 2'),
        (4, 'Table for 4'),
        (8, 'Table for 8'),
        (12, 'Table for 12'),
        (20, 'Table for 20'),
    ]

    tableID = models.AutoField(primary_key=True)
    tableSize = models.IntegerField(choices=tableSize_choices)

    def __str__(self):
        return f"Table {self.tableID} - {self.get_tableSize_display()}"


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
    table = models.ForeignKey(Table, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Reservation for {self.UserID.UserFirstName} {self.UserID.UserLastName} on {self.Date} at {self.TimeOfReservation}"

    def select_table(self):
        if self.TimeOfReservation is None:
            raise ValidationError("Time of reservation is required to select a table.")

        if self.table:
            raise ValidationError("A table has already been selected for this reservation.")

        # Find an available table based on table size
        available_tables = Table.objects.filter(tableSize=self.tableSize, reservation__isnull=True)

        if not available_tables:
            raise ValidationError("No available tables for this table size.")

        table = available_tables.first()
        table.reservation = self
        table.save()


class Employee(models.Model):
    EmployeeID = models.AutoField(primary_key=True)
    HireDate = models.DateField()
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Position = models.CharField(max_length=50)
    Address1 = models.CharField(max_length=100)
    Address2 = models.CharField(max_length=100, blank=True, null=True)
    City = models.CharField(max_length=50)

    STATE_CHOICES = (
        ('Nebraska', 'Nebraska'),
        ('Iowa', 'Iowa'),
    )
    State = models.CharField(max_length=50, choices=STATE_CHOICES)

    ZipCode = models.CharField(max_length=5, validators=[RegexValidator(
        regex=r'^\d{5}$',
        message='Zip code must be exactly 5 digits.',
    )])

    PhoneNum = models.CharField(max_length=12, validators=[RegexValidator(
        regex=r'^\(\d{3}\)-\d{3}-\d{4}$',
        message='Phone number must be in the format (###)-###-####.',
    )])

    Password = models.CharField(max_length=128)  # Hash the password using Django's authentication system

    def __str__(self):
        return f"{self.FirstName} {self.LastName}"


class FoodMenu(models.Model):
    MENU_CATEGORIES = [
        ('Appetizers', 'Appetizers'),
        ('Soups and Salads', 'Soups and Salads'),
        ('Sandwiches & Burgers', 'Sandwiches & Burgers'),
        ('Main Entrees', 'Main Entrees'),
        ('Desserts', 'Desserts'),
        ('Sides', 'Sides'),
        ('Drinks', 'Drinks'),
    ]

    FOOD_SIZES = [
        ('Tiny Ones', 'Tiny Ones'),
        ('Small Kid', 'Small Kid'),
        ('Big Kid', 'Big Kid'),
        ('Teen', 'Teen'),
        ('Adult', 'Adult'),
    ]

    MenuID = models.AutoField(primary_key=True)
    foodCategory = models.CharField(max_length=20, choices=MENU_CATEGORIES)
    foodName = models.CharField(max_length=100)
    foodPic = models.ImageField(upload_to='food_pics/')
    foodSize = models.CharField(max_length=20, choices=FOOD_SIZES)
    foodPrice = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.foodName


class Payment(models.Model):
    PaymentID = models.AutoField(primary_key=True)
    userSelect = models.BooleanField()
    nameOnCard = models.CharField(max_length=100)
    cardNumber = models.CharField(max_length=19)
    expDate = models.CharField(max_length=6)
    cvv = models.CharField(max_length=3)
    ZipCode = models.CharField(max_length=5)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payments')

    def __str__(self):
        return f"PaymentID: {self.PaymentID}"

    def save(self, *args, **kwargs):
        # Automatically set nameOnCard and ZipCode based on the associated User
        if self.user:
            self.nameOnCard = f"{self.user.UserFirstName} {self.user.UserLastName}"
            self.ZipCode = self.user.ZipCode
        super().save(*args, **kwargs)
