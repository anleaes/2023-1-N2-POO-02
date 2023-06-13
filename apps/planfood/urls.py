from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'planfood'

router = routers.DefaultRouter()
router.register('planfood', views.CategoryViewSet, basename='planfood')

urlpatterns = [
    path('', include(router.urls) )
]