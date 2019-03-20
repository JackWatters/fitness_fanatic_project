from fitness.models import Workout, Exercise
import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'fitness_fanatic_project.settings')

django.setup()


def populate():
    workouts = {
        "The Ultimate Half Marathon": {
            "description": "This half-marathon workout is designed to test the athlete 2-3 months before a half-marathon race. It consists of breaking the marathon into six-hour intervals",
            "views": 36,
        },
        "workout2": {
            "description": "an example of workout 2",
            "views": 50,
        },
        "popular workout": {
            "description": "A very popular workout",
            "views": 3000,
        },
        "unpopular workout": {
            "description": "an example of workout 1",
            "views": 0,
        }
    }

    for workout, workoutInfo in workouts.items():
        w = add_workout(
            workout, workoutInfo["description"], workoutInfo["views"])


def add_workout(title, description, views):
    w = Workout.objects.get_or_create(
        title=title, description=description, views=views)[0]
    w.save()


if __name__ == '__main__':
    print("Starting FitnessFanatic population script...")
    populate()
