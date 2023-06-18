from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'plans'

router = routers.DefaultRouter()
router.register('planos', views.PlansViewSet, basename='planos')

urlpatterns = [
    path('', include(router.urls) )
]