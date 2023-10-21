# Generated by Django 4.2.5 on 2023-10-21 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='TimeOfReservation',
            field=models.TimeField(choices=[('11:00:00', '11:00 AM'), ('11:15:00', '11:15 AM'), ('11:30:00', '11:30 AM'), ('11:45:00', '11:45 AM'), ('12:00:00', '12:00 PM'), ('12:15:00', '12:15 PM'), ('12:30:00', '12:30 PM'), ('12:45:00', '12:45 PM'), ('13:00:00', '01:00 PM'), ('13:15:00', '01:15 PM'), ('13:30:00', '01:30 PM'), ('13:45:00', '01:45 PM'), ('14:00:00', '02:00 PM'), ('14:15:00', '02:15 PM'), ('14:30:00', '02:30 PM'), ('14:45:00', '02:45 PM'), ('15:00:00', '03:00 PM'), ('15:15:00', '03:15 PM'), ('15:30:00', '03:30 PM'), ('15:45:00', '03:45 PM'), ('16:00:00', '04:00 PM'), ('16:15:00', '04:15 PM'), ('16:30:00', '04:30 PM'), ('16:45:00', '04:45 PM'), ('17:00:00', '05:00 PM'), ('17:15:00', '05:15 PM'), ('17:30:00', '05:30 PM'), ('17:45:00', '05:45 PM'), ('18:00:00', '06:00 PM'), ('18:15:00', '06:15 PM'), ('18:30:00', '06:30 PM'), ('18:45:00', '06:45 PM'), ('19:00:00', '07:00 PM'), ('19:15:00', '07:15 PM'), ('19:30:00', '07:30 PM'), ('19:45:00', '07:45 PM'), ('20:00:00', '08:00 PM'), ('20:15:00', '08:15 PM'), ('20:30:00', '08:30 PM'), ('20:45:00', '08:045 PM'), ('21:00:00', '09:00 PM')]),
        ),
    ]
