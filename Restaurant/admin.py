from django.contrib import admin
from .models import Menu, Booking

# Register your models here.
admin.site.register(Menu)
admin.site.register(Booking)

# Superuser account:
# ID: admin
# Password: password

# User1:
# ID: user1
# Password: Password123!