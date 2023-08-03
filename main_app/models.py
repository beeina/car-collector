from django.db import models
from django.urls import reverse

# Create your models here.

class Car(models.Model):
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    features = models.CharField(max_length=100)
    year = models.IntegerField()
    model = models.CharField(max_length=100)
    countryItMade = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.brand} {self.id} {self.model} {self.features} {self.year}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})