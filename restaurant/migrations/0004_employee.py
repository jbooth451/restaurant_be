# Generated by Django 4.2.5 on 2023-10-21 17:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_alter_reservation_timeofreservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('EmployeeID', models.AutoField(primary_key=True, serialize=False)),
                ('HireDate', models.DateField()),
                ('FirstName', models.CharField(max_length=50)),
                ('LastName', models.CharField(max_length=50)),
                ('Position', models.CharField(max_length=50)),
                ('Address1', models.CharField(max_length=100)),
                ('Address2', models.CharField(blank=True, max_length=100, null=True)),
                ('City', models.CharField(max_length=50)),
                ('State', models.CharField(choices=[('Nebraska', 'Nebraska'), ('Iowa', 'Iowa')], max_length=50)),
                ('ZipCode', models.CharField(max_length=5, validators=[django.core.validators.RegexValidator(message='Zip code must be exactly 5 digits.', regex='^\\d{5}$')])),
                ('PhoneNum', models.CharField(max_length=12, validators=[django.core.validators.RegexValidator(message='Phone number must be in the format (###)-###-####.', regex='^\\(\\d{3}\\)-\\d{3}-\\d{4}$')])),
                ('Password', models.CharField(max_length=128)),
            ],
        ),
    ]