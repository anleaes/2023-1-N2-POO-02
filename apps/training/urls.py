from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'training'

router = routers.DefaultRouter()
router.register('training', views.CategoryViewSet, basename='training')

urlpatterns = [
    path('', include(router.urls) )
]