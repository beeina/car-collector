from django.db import models
from django.urls import reverse

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("users_detail", kwargs={"pk": self.id})
    

class Car(models.Model):
    brand = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    features = models.CharField(max_length=100)
    year = models.IntegerField()
    model = models.CharField(max_length=100)
    countryItMade = models.CharField(max_length=100)
    # Create M:M relationship with User
    users = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.brand} {self.id} {self.model} {self.features} {self.year}'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'car_id': self.id})
    
    
class Insurance(models.Model):
        policyNumber = models.IntegerField()
        provider = models.CharField(max_length=100)
        coverageAmount = models.IntegerField()
        startDate = models.DateField('Starting Date') 
        endDate = models.DateField('Ending Date') 

        car = models.ForeignKey(
            Car, 
            on_delete=models.CASCADE
        )

        def __str__(self):
            return f'{self.policyNumber} {self.provider} {self.coverageAmount} {self.startDate} {self.endDate}'
        
    

