from django.db import models

# Create your models here.
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()
    # item = models.CharField(max_length=100)
    # price = models.IntegerField()
    def __str__(self):
        return f"{self.title}"

class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guest = models.IntegerField()
    booking_date = models.DateTimeField(default=None)
    # tableno = models.IntegerField()
    # persons = models.IntegerField()
    def __str__(self):
        return f"{self.name}, {self.booking_date}, for {self.no_of_guest} people"