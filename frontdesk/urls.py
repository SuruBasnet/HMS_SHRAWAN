from django.urls import path
from .views import *

urlpatterns = [
    path('guestinfo/all/',guestInfoApiView,name='guestinfo')
]