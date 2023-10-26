from django.db import models

from django.contrib.auth.models import User

savepath = "static/rooms/"
class Hostel(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    telno=models.CharField(max_length=15)
    email=models.CharField(max_length=30)
    status=models.CharField(max_length=20, default="not approved")
    image=models.ImageField(upload_to='static/hostel')
    manager=models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class Feedback(models.Model):
    rating=models.DecimalField(max_digits=5, decimal_places=2)
    comment=models.CharField(max_length=200)
    date=models.DateTimeField(auto_now_add=True)
    student=models.ForeignKey(User,on_delete=models.CASCADE)
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.comment
class Room(models.Model):
    room_number=models.CharField(max_length=6, unique=True)
    occupants = models.DecimalField(max_digits=5, decimal_places=0, default=0)
    hostel=models.ForeignKey(Hostel, on_delete=models.CASCADE)
    reservation=models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    image0 = models.ImageField(upload_to=savepath, null=True, blank = True)
    image1 = models.ImageField(upload_to=savepath, null=True, blank = True)
    image2 = models.ImageField(upload_to=savepath, null=True, blank = True)
    image3 = models.ImageField(upload_to=savepath, null=True, blank = True)
    def __str__(self):
        return self.room_number

class Payment(models.Model):
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    paymentDate=models.DateField(auto_now_add=True)
    paymentMethod=models.CharField(max_length=20)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)

class Reservation(models.Model):
    checkInDate=models.DateField()
    checkOutDate=models.DateField()
    student=models.ForeignKey(User, on_delete=models.CASCADE)
    payment=models.ForeignKey(Payment, on_delete=models.CASCADE)


# Create your models here.
