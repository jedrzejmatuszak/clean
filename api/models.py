from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Flat(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.TextField()
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Clean(models.Model):
    name = models.TextField()
    points = models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Flatmate(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    flat = models.ForeignKey(Flat, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        if self.username.first_name != '':
            return str(self.username.get_full_name())
        else:
            return self.username.username


class Record(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, null=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    clean = models.ForeignKey(Clean, on_delete=models.CASCADE, null=True)
    flatmate = models.ForeignKey(Flatmate, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    to_date = models.DateField()
    realized = models.BooleanField(default=False)
    points = models.IntegerField()
