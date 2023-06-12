from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'gym'

router = routers.DefaultRouter()
router.register('gym', views.ProductViewSet, basename='gym')

urlpatterns = [
    path('', include(router.urls) )
]