from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'main-home'),
    path('servis/', views.servis, name = 'main-servis'),
]
