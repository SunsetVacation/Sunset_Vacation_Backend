from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core import views

router = DefaultRouter()

urlpatterns = [
    path('login/', views.login, name="login"),

]
