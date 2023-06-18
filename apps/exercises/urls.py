from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'exercises'

router = routers.DefaultRouter()
router.register('exercicios', views.ExercisesViewSet, basename='exercises')

urlpatterns = [
    path('', include(router.urls) )
]