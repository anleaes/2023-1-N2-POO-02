from django.urls import path, include
from . import views
from rest_framework import routers
app_name = 'students'

router = routers.DefaultRouter()
router.register('estudantes', views.StudentsViewSet, basename='students')

urlpatterns = [
    path('', include(router.urls) )
]