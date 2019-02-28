from django.contrib import admin
from fitness.models import Workout, Exercise
from fitness.models import UserProfile

admin.site.register(Workout)
admin.site.register(Exercise)
admin.site.register(UserProfile)
