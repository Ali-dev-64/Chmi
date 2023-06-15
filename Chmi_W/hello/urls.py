from django.urls import path
from . import views
urlpatterns=[
    path("", views.Home,name="home"),
    path("ele",views.Chmi_Ele,name="Chmi_Ele"),
    path("ran", views.ran,name="Ran")
]