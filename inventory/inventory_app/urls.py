from django.urls import path

from . import views

# This is the url dispatcher to route requests to views (objects that handles responses)
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:id>", views.delete, name="delete"),
]