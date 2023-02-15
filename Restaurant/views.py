from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Menu, Booking
from .serializers import MenuItemSerializer, BookingSerializer

# Create your views here.
def sayHello(request):
    return HttpResponse('Hello World')

def index(request):
    return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    # def get_permissions(self):
    #     permission_classes = []
    #     if self.request.method != 'GET':
    #         permission_classes = []
    #     return [permission() for permission in permission_classes]

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    # def get_permissions(self):
    #     permission_classes = []
    #     if self.request.method != 'GET':
    #         permission_classes = [IsAuthenticated]
    #     return [permission() for permission in permission_classes]

class BookingView(APIView):
    def get(self, request):
        items = Booking.objects.all()
        serializer = BookingSerializer(items, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})