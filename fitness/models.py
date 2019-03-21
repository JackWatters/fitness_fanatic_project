from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

class Workout(models.Model):
    length_max = 128
    title = models.CharField(max_length=length_max, unique=True)
    description = models.TextField(max_length=280,blank=True)
    image = models.ImageField(upload_to ='workout_images',blank=True)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique = True)

    likes = models.ManyToManyField(User, related_name = 'likes', blank = True)
    favourite = models.ManyToManyField(User, related_name = 'favourite', blank = True)
    
    author = models.IntegerField(default=0)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Workout, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_workout', args=[self.slug])

    def total_likes(self):
        return self.likes.count()

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

    favourites = models.ManyToManyField(Workout, related_name = 'favourites', blank = True)
    
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username

