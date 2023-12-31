from rest_framework import serializers
from .models import FoodMenu, Payment, Order, Table, OrderFoodItem, Reservation
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodMenu
        fields = ('MenuID', 'foodCategory', 'foodName', 'foodPic', 'foodSize', 'foodPrice',)


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'},
                                     validators=[validate_password])
    password2 = serializers.CharField(write_only=True, style={'input_type': 'password'}, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            'password': {'write_only': True, 'min_length': 6},
            'password2': {'write_only': True, 'min_length': 6}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

'''
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('EmployeeID', 'HireDate', 'FirstName', 'LastName', 'Position', 'Address1', 'Address2', 'City', 'State', 'ZipCode', 'PhoneNum', 'Password')
'''
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('PaymentID', 'userSelect', 'nameOnCard', 'cardNumber', 'expDate', 'cvv', 'ZipCode', 'user')

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ('tableID', 'tableSize')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('OrderID', 'OrderDate', 'OrderTime', 'user', 'food_items', 'table', 'payment')

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ('ReservationID', 'TimeOfReservation', 'Date', 'UserID', 'table')
