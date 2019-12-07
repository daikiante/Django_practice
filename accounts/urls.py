from django.urls import path
from . import views

urlpatterns = [
    path('acount/', views.all_info)
]
