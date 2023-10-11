from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework.response import Response

# Create your views here.
# def home(request): # For template based django project
#     return render()

# Request methods - Get, Post, Put, Patch , Delete

@api_view(['GET'])
def guestInfoApiView(request):
    queryset = GuestInfo.objects.all()
    serializer = GuestInfoSerializer(queryset,many=True)
    return Response(serializer.data)
