from django.shortcuts import render

cars = [
   {'brand': 'Honda',
    'color': 'metalic grey',
    'model': 'CR-V',
    'year': '2020',
    'countryItMade': 'Japan'
    },
    {'brand': 'Tesla',
     'color': 'white',
     'model': 'Y',
     'year': '2021',
     'countryItMade': 'USA'
     },
     {'brand': 'Lexus',
      'color': 'black',
      'model': 'RC F',
      'year': '2022',
      'countryItMade': 'USA'}
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def cars_index(request):
  return render(request, 'cars/index.html', {
    'cars': cars
  })