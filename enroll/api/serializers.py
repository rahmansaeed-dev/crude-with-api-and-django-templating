from enroll.models import User
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','name','email','password']




