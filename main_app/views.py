from django.shortcuts import render, redirect

#import model here
from .models import Car, User
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from .forms import InsuranceForm


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
  id_list = car.users.all().values_list('id')
  users_car_doesnt_have = User.objects.exclude(id__in=id_list)
  insurance_form = InsuranceForm()
  return render(request, 'cars/detail.html', {"car": car, 'insurance_form': insurance_form, 'users': users_car_doesnt_have})

class CarCreate(CreateView):
   model = Car
   fields = ['brand', 'color', 'model', 'features', 'year', 'countryItMade']
  

class CarUpdate(UpdateView):
  model = Car
  fields = ['brand', 'color', 'model', 'features', 'year', 'countryItMade']

class CarDelete(DeleteView):
  model = Car
  success_url = '/cars'

def add_insurance(request, car_id):
  
  form = InsuranceForm(request.POST)
  if form.is_valid():
    new_insurance = form.save(commit=False)
    new_insurance.car_id = car_id
    new_insurance.save()
  return redirect('detail', car_id=car_id)

class UserList(ListView):
  model = User

class UserDetail(DetailView):
  model = User

class UserCreate(CreateView):
  model = User
  fields = '__all__'

class UserUpdate(UpdateView):
  model = User
  fields = ['name']

class UserDelete(DeleteView):
  model = User
  success_url = '/users'

def assoc_user(request, car_id, user_id):
  Car.objects.get(id=car_id).users.add(user_id)
  return redirect('detail', car_id=car_id)

def unassoc_user(request, car_id, user_id):
  Car.objects.get(id=car_id).users.remove(user_id)
  return redirect('detail', car_id=car_id)


