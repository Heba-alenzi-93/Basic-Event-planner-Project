from enum import unique
from django.db import models

# Create your models here.



class EvenPlanner (models.Model):
     organizer = models.CharField(max_length=20,unique = True)
     name =  models.CharField(max_length=100)
     email = models.CharField(max_length=100)
     image = models.CharField(max_length=250)
     num_of_seat = models.PositiveIntegerField()
     booked_seats =  models.PositiveIntegerField()
     start_date =  models.DateField()
     end_date = models.DateField()

     def __str__(self):
        return self.name




