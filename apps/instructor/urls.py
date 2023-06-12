from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'instructor'

router = routers.DefaultRouter()
router.register('instructor', views.InstructorViewSet, basename='instructor')

urlpatterns = [
    path('', include(router.urls) )
]