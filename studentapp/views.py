from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from .models import Student
from .serializers import StudentSerailizer
from rest_framework.response import Response


# Create your views here.
class StudentView(APIView):
    def get(self,request):
        data = Student.objects.all()
        studentdata=StudentSerailizer(data,many=True).data
        return Response(studentdata)

    def post(self, request):
        serializer = StudentSerailizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

