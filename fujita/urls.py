from django.urls import path
from . import views

urlpatterns = [
    path('fujisan', views.home),
]