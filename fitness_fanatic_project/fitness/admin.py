from django.contrib import admin
from fitness.models import Workout, Exercise, UserProfile

class WorkoutAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

admin.site.register(Workout, WorkoutAdmin)
admin.site.register(Exercise)
admin.site.register(UserProfile)
