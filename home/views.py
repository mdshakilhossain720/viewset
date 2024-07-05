from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .models import Studetn
from.serilazers import StudentSerilazer


# Create your views here.

class StudentLIst(viewsets.ViewSet):
    def list(self,request):
        stu=Studetn.objects.all()
        serilazers=StudentSerilazer(stu,many=True)
        return Response(serilazers.data)
    
    


