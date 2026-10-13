from django.urls import path
from . import views

urlpatterns = [
    path("<int:month>" , views.handel_month_by_number),
    path("<str:month>" , views.handel_month),
]