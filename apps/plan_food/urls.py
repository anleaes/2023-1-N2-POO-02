from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'plan_food'

router = routers.DefaultRouter()
router.register('plan_food', views.CategoryViewSet, basename='plan_food')

urlpatterns = [
    path('', include(router.urls) )
]