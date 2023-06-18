from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'trainings'

router = routers.DefaultRouter()
router.register('treinos', views.TrainingsViewSet, basename='treinos')

urlpatterns = [
    path('', include(router.urls) )
]