from django.urls import path
from . import views

urlpatterns = [
    path('say-hello/', views.sayHello, name='sayHello'),
    path('', views.index, name='index'),
    path('api/menu/', views.MenuItemsView.as_view()),
    path('api/menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('menu/', views.MenuItemsView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
    path('api/booking/', views.BookingView.as_view()),
]