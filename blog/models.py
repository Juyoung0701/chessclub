from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Chessuser(models.Model):

    name = models.CharField(max_length=20)
    points = models.IntegerField(default=2000)
    rank = models.CharField(max_length=20, default="null")
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    win = models.IntegerField(default=0)
    lose = models.IntegerField(default=0)
    
    
    class Meta:
        ordering = ('-points',)


    def __str__(self):
        return self.name



    