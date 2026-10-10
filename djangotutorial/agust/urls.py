from django.urls import path
from . import views

urlpatterns = [
    path("agust", views.agust),
    path("sep", views.sep)
]