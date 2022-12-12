from django.urls import path, include
from .views import index
from store import views

urlpatterns = [
    path('index/', views.index, name='index')
]