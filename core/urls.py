from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core import views

router = DefaultRouter()
# router.register('profiles', views.ProfileList, basename="profiles")

urlpatterns = [
    path('', views.ProfileListView.as_view()),
    path('<int:id>/', views.ProfileListView.as_view()),
    # path('', views.profile, name='profile'),
    # path('password/', views_user.password, name='password'),
    path('', include(router.urls))
]
