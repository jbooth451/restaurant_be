from rest_framework import status, generics
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.contrib.auth.models import User
from .serializers import RegisterSerializer

@api_view(['GET', 'POST'])
def food_menu(request):
    if request.method == 'GET':
        foodmenu = FoodMenu.objects.all()
        serializer = MenuSerializer(foodmenu, context={'request': request}, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = MenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def getMenu(request, pk):
    """
    Retrieve, update or delete a movie instance.
    """
    try:
        menu = FoodMenu.objects.get(pk=pk)
    except FoodMenu.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MenuSerializer(menu,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = MenuSerializer(menu, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RegisterView(generics.CreateAPIView):
     queryset = User.objects.all()
     permission_classes = (AllowAny,)
     serializer_class = RegisterSerializer

@api_view(['GET', 'POST'])
def employee(request):
    if request.method == 'GET':
        employee1 = Employee.objects.all()
        serializer = EmployeeSerializer(employee1, context={'request': request}, many=True)
        return Response({'data': serializer.data})

    elif request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def getEmployee(request, pk):
    """ Retrieve, update or delete a movie instance."""
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee, context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
