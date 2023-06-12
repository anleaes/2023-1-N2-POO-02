from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'food_plan'

router = routers.DefaultRouter()
router.register('food_plan', views.CategoryViewSet, basename='food_plan')

urlpatterns = [
    path('', include(router.urls) )
]