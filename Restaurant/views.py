from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Menu, Booking
from .serializers import UserSerializer, MenuItemSerializer, BookingSerializer
from django.contrib.auth.models import User

# Create your views here.
def sayHello(request):
    return HttpResponse('Hello World')

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer

class BookingViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]