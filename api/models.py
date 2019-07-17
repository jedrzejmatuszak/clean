from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Flat(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.TextField()
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, null=True, related_name='rooms')

    def __str__(self):
        return f'{self.name} - {self.flat.name}'


class CleanUp(models.Model):
    name = models.TextField()
    points = models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, related_name='cleanup')

    def __str__(self):
        return self.name


class Flatmate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flat = models.ForeignKey(Flat, on_delete=models.SET_NULL, null=True, related_name='flatmates')

    def __str__(self):
        if self.user.first_name != '':
            return str(self.user.get_full_name())
        else:
            return self.user.username


class Record(models.Model):
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE, null=True, related_name='flat_records')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True, related_name='room_records')
    cleanup = models.ForeignKey(CleanUp, on_delete=models.CASCADE, null=True, related_name='cleanup_records')
    flatmate = models.ForeignKey(Flatmate, on_delete=models.CASCADE, null=True, related_name='flatmate_records')
    date = models.DateTimeField(auto_now_add=True, null=True)
    to_date = models.DateField()
    realized = models.BooleanField(default=False)
    points = models.IntegerField()

    def __str__(self):
        return f"{self.room} - {self.cleanup} - {self.flatmate} - {self.to_date}"
