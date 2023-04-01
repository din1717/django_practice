from rest_framework.serializers import ModelSerializer
from .models import Student


class StudentSerailizer(ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
