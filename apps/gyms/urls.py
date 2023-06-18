from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'gyms'

router = routers.DefaultRouter()
router.register('academias', views.GymsViewSet, basename='academias')

urlpatterns = [
    path('', include(router.urls) )
]