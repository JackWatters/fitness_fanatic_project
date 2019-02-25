from django.db import models

class Workout(models.Model):
    title = models.CharField(max_length=128, unique=True)
    description = models.TextField(max_length=280)
    image = models.ImageField(upload_to ='workout_images')
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

class Exercise(models.Model):
    workout = models.ForeignKey(Workout)
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=280)
    image = models.ImageField(upload_to ='exercise_images')
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

