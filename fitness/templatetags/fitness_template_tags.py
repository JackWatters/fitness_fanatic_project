from django import template
from fitness.models import Workout

register = template.Library()

@register.inclusion_tag('fitness/workouts.html')
def get_workout_list():
    return {'workouts': Workout.objects.all()}