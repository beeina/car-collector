from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.cars_index, name='index'),
    path('cars/<int:car_id>', views.cars_detail, name="detail"),
    path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
    path('cars/<int:car_id>/add_insurance/', views.add_insurance, name='add_insurance'),
    path('cars/<int:car_id>/assoc_user/<int:user_id>/', views.assoc_user, name='assoc_user'),
    path('cars/<int:car_id>/unassoc_user/<int:user_id>/', views.unassoc_user, name='unassoc_user'),
    path('users/', views.UserList.as_view(), name='users_index'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='users_detail'),
    path('users/create/', views.UserCreate.as_view(), name='users_create'),
    path('users/<int:pk>/update/', views.UserUpdate.as_view(), name='users_update'),
    path('users/<int:pk>/delete/', views.UserDelete.as_view(), name='users_delete'),
]

