from django.db import models
from django.contrib.auth.models import User

class Workout(models.Model):
    length_max = 128
    title = models.CharField(max_length=length_max, unique=True)
    description = models.TextField(max_length=280,blank=True)
    image = models.ImageField(upload_to ='workout_images',blank=True)
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

class Exercise(models.Model):
    workout = models.ForeignKey(Workout)
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=280,blank=True)
    image = models.ImageField(upload_to ='exercise_images',blank=True)
    views = models.IntegerField(default=0,blank=True)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

