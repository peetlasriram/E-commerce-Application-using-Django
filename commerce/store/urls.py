from django.urls import path
from .views import home, view

urlpatterns = [
    path("",view, name="home"),

]