from django.urls import path
from . import views

urlpatterns = [
    path('say-hello/', views.sayHello, name='sayHello'),
    path('', views.index, name='index'),
    path('api/menu/', views.MenuView.as_view()),
    path('api/booking/', views.BookingView.as_view()),
]