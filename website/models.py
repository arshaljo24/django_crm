from django.db import models


class Record(models.Model):
     created_at = models.DateTimeField(auto_now_add=True)
     firstname =models.CharField(max_length=50)
     lastname = models.CharField(max_length=50)
     email =models.CharField(max_length=100)
     phone = models.CharField(max_length=20)
     address = models.CharField(max_length=100)
     city = models.CharField(max_length=30)
     state = models.CharField(max_length=30)
     zipcode = models.CharField(max_length=10)


     def __str__(self):
         return (f"{self.firstname} {self.lastname}")






