from django.db import models

class customer(models.Model):
    id_number = models.IntegerField(null=False, default=0)
    name = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    No_of_tickets = models.IntegerField(null=True)
    paid = models.CharField(default='not paid')

# Create your models here.
