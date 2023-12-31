# Generated by Django 4.2.5 on 2023-10-30 22:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodMenu',
            fields=[
                ('MenuID', models.AutoField(primary_key=True, serialize=False)),
                ('foodCategory', models.CharField(choices=[('Appetizers', 'Appetizers'), ('Soups and Salads', 'Soups and Salads'), ('Sandwiches & Burgers', 'Sandwiches & Burgers'), ('Main Entrees', 'Main Entrees'), ('Desserts', 'Desserts'), ('Sides', 'Sides'), ('Drinks', 'Drinks')], max_length=20)),
                ('foodName', models.CharField(max_length=100)),
                ('foodPic', models.ImageField(upload_to='food_pics/')),
                ('foodSize', models.CharField(choices=[('Tiny Ones', 'Tiny Ones'), ('Small Kid', 'Small Kid'), ('Big Kid', 'Big Kid'), ('Teen', 'Teen'), ('Adult', 'Adult')], max_length=20)),
                ('foodPrice', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('OrderID', models.AutoField(primary_key=True, serialize=False)),
                ('OrderDate', models.DateField(auto_now_add=True)),
                ('OrderTime', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('tableID', models.AutoField(primary_key=True, serialize=False)),
                ('tableSize', models.IntegerField(choices=[(2, 'Table for 2'), (4, 'Table for 4'), (8, 'Table for 8'), (12, 'Table for 12'), (20, 'Table for 20')])),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('ReservationID', models.AutoField(primary_key=True, serialize=False)),
                ('TimeOfReservation', models.CharField(choices=[('11:00:00', '11:00 AM'), ('11:15:00', '11:15 AM'), ('11:30:00', '11:30 AM'), ('11:45:00', '11:45 AM'), ('12:00:00', '12:00 PM'), ('12:15:00', '12:15 PM'), ('12:30:00', '12:30 PM'), ('12:45:00', '12:45 PM'), ('13:00:00', '01:00 PM'), ('13:15:00', '01:15 PM'), ('13:30:00', '01:30 PM'), ('13:45:00', '01:45 PM'), ('14:00:00', '02:00 PM'), ('14:15:00', '02:15 PM'), ('14:30:00', '02:30 PM'), ('14:45:00', '02:45 PM'), ('15:00:00', '03:00 PM'), ('15:15:00', '03:15 PM'), ('15:30:00', '03:30 PM'), ('15:45:00', '03:45 PM'), ('16:00:00', '04:00 PM'), ('16:15:00', '04:15 PM'), ('16:30:00', '04:30 PM'), ('16:45:00', '04:45 PM'), ('17:00:00', '05:00 PM'), ('17:15:00', '05:15 PM'), ('17:30:00', '05:30 PM'), ('17:45:00', '05:45 PM'), ('18:00:00', '06:00 PM'), ('18:15:00', '06:15 PM'), ('18:30:00', '06:30 PM'), ('18:45:00', '06:45 PM'), ('19:00:00', '07:00 PM'), ('19:15:00', '07:15 PM'), ('19:30:00', '07:30 PM'), ('19:45:00', '07:45 PM'), ('20:00:00', '08:00 PM'), ('20:15:00', '08:15 PM'), ('20:30:00', '08:30 PM'), ('20:45:00', '08:45 PM'), ('21:00:00', '09:00 PM')], max_length=30)),
                ('Date', models.DateField()),
                ('UserID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to=settings.AUTH_USER_MODEL)),
                ('table', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.table')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('PaymentID', models.AutoField(primary_key=True, serialize=False)),
                ('userSelect', models.BooleanField()),
                ('nameOnCard', models.CharField(max_length=100)),
                ('cardNumber', models.CharField(max_length=19)),
                ('expDate', models.CharField(max_length=6)),
                ('cvv', models.CharField(max_length=3)),
                ('ZipCode', models.CharField(max_length=5)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderFoodItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('food_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.foodmenu')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='food_items',
            field=models.ManyToManyField(through='restaurant.OrderFoodItem', to='restaurant.foodmenu'),
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.payment'),
        ),
        migrations.AddField(
            model_name='order',
            name='table',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='restaurant.table'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
    ]
