from django.shortcuts import render, redirect

#import model here
from .models import Car 
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# from .forms import InsuranceForm

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

class CarCreate(CreateView):
   model = Car
   fields = ['brand', 'color', 'model', 'features', 'year', 'countryItMade']
  

class CarUpdate(UpdateView):
  model = Car
  fields = ['brand', 'color', 'model', 'features', 'year', 'countryItMade']

class CarDelete(DeleteView):
  model = Car
  success_url = '/cars'

# def add_insurance(request, car_id):
#   form = InsuranceForm(request,POST)
#   if form.is_valid():
#     new_insurance = form.save(commit=False)
#     new_insurance.car_id = car_id
#     new_insurance.save()
#   return redirect('detail', car_id=car_id)
