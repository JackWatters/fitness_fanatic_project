import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from fitness.models import Workout, Exercise

def populate():
    workouts = {
        "workout1": {
            "description": "an example of workout 1",
            "views": 36,
        },
        "workout2": {
            "description": "an example of workout 2",
            "views": 50,
        },
        "popular workout": {
            "description": "an example of workout 1",
            "views": 3000,
        },
        "unpopular workout": {
            "description": "an example of workout 1",
            "views": 0,
        }
    }

    for workout, workoutInfo in workouts.items():
        w = add_workout(workout, workoutInfo["description"], workoutInfo["views"])

def add_workout(title, description, views):
    w = Workout.objects.get_or_create(title=title, description=description, views=views)[0]
    w.save()



if __name__ == '__main__':
    print("Starting FitnessFanatic population script...")
    populate()