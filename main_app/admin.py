from django.contrib import admin

from .models import Car, Insurance, User

# Register your models here.
admin.site.register(Car)
admin.site.register(Insurance)
admin.site.register(User)

