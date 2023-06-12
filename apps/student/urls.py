from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'student'

router = routers.DefaultRouter()
router.register('student', views.StudentViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls) )
]
