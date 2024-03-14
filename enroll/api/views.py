from rest_framework import serializers
from enroll.models import User
from .serializers import StudentSerializer
from rest_framework import viewsets
class StudentSerializerView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = StudentSerializer






