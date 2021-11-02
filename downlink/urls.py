from django.urls import path

from . import views

app_name = "downlink"
urlpatterns = [
    path("", views.index, name="index")
]