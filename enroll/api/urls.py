from django.urls import path, include
from rest_framework.routers import DefaultRouter
from enroll.api.views import StudentSerializerView

router = DefaultRouter()

router.register('student', StudentSerializerView, basename='student')

urlpatterns = [
    path('', include(router.urls)),
]



