from django.shortcuts import render

#import model here
from .models import Car 


# cars = [
#    {'brand': 'Honda',
#     'color': 'metalic grey',
#     'model': 'CR-V',
#     'features': 'two-motor hybrid powertrain',
#     'year': '2020',
#     'countryItMade': 'Japan'
#     },
#     {'brand': 'Tesla',
#      'color': 'white',
#      'model': 'Y',
#      'features': 'dual motor',
#      'year': '2021',
#      'countryItMade': 'USA'
#      },
#      {'brand': 'Lexus',
#       'color': 'black',
#       'model': 'RC F',
#       'features': 'bolder styling',
#       'year': '2022',
#       'countryItMade': 'USA'}
# ]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cars_index(request):
  cars = Car.objects.all() 
  return render(request, 'cars/index.html', {
    'cars': cars
  })

def cars_detail(request, car_id):
  car = Car.objects.get(id=car_id)
  return render(request, 'cars/detail.html', {"car": car})