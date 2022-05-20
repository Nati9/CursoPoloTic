from django.urls import path
from . import views

app_name = "TAREAS"
urlpatterns = [
    path('', views.index, name="index"),
    path('agregar', views.agregar, name="agregar")
]