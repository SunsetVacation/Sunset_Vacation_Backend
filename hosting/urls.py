from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

urlpatterns = [
    path('categories/', views.getCategories, name="getCategories"),
    path('subcategories/', views.getSubCategories, name="getSubCategories"),
]
