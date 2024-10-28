from django.urls import path
from . import views

urlpatterns = [
    path('crearusuario/', views.register, name='register'),
]
