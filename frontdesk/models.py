from django.db import models

# Create your models here.
class GuestInfo(models.Model):
    f_name = models.CharField(max_length=200)
    l_name = models.CharField(max_length=200)
    address = models.TextField()
    phone_number = models.IntegerField()
    email = models.EmailField(unique=True)

class RoomType(models.Model):
    name = models.CharField(max_length=200)

class Room(models.Model):
    room_status = [('Occupied','Occupied'),('Available','Available')]

    room_no = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20,choices=room_status)
    floor = models.CharField(max_length=50)
    room_type = models.ForeignKey(RoomType,on_delete=models.SET_NULL,null=True)

class GuestRoom(models.Model):
    guest = models.ForeignKey(GuestInfo,on_delete=models.CASCADE)
    room_no = models.ForeignKey(Room,on_delete=models.CASCADE)
    checked_out = models.BooleanField(default=False)

