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
        "Supermans": {
            "description": "Lie prone (on your stomach) on a mat with your legs extended, ankles slightly plantarflexed (toes pointing away from your shins), arms extended overhead with palms facing each other. Relax your head to align it with your spine.  Exhale, contract your abdominal and core muscles to stabilize your spine and slowly extend both hips (raise both legs) a few inches off the floor while simultaneously raising both arms a few inches off the floor. Gently inhale and lower your legs and arms back towards your starting position without any movement in your low back or hips.",
            "views": 50,
        },
        "Contralateral Limb Raises": {
            "description": "Lie prone (on your stomach) on a mat with your legs extended. Exhale, contract your abdominal/core muscles to stabilize your spine and slowly raise one arm a few inches off the floor keeping your arm extended and avoiding any rotation in your arm. Maintain your head and torso position, avoiding any arching in your back or raising of your head. Hold this position briefly. Gently inhale and lower your arm back towards your starting position without any movement in your low back or hips. rom your starting position, contract your abdominal/core muscles to stabilize your spine and slowly extend one hip (raise one leg) a few inches off the floor while simultaneously raising the opposite arm a few inches off the floor.  Hold this position briefly before returning to your starting position.",
            "views": 3000,
        },
        "Downward-facing Dog": {
            "description": "Kneel on an exercise mat or floor and bring your feet together behind you. Slowly bend forward to place your palms flat on the mat, positioning your hands shoulder-width apart with your fingers facing forward. Slowly lift yourself into a push-up position, shifting your hands until your shoulders are positioned directly over your hands. hile maintaining a rigid torso and full extension in your arms and legs, slowly exhale and shift your weight backwards by pushing your hips backwards and upwards. Maintain your head alignment with your spine, but slowly move your head between your shoulders as your body moves backwards and attempt to push your heels towards the floor. Maintain the stiffness in your torso to prevent the tendency of your back to arch. Continue moving until your body forms an inverted-V. Inhale and return your body to the starting push-up position, maintaining the alignment of all your body segments.",
            "views": 0,
        }
		 "Front Plank": {
            "description": "Lie prone (on your stomach) on an exercise mat or floor with your elbows close to your sides and directly under your shoulders, palms down and hands facing forward. Slowly lift your entire torso off the floor or mat, maintaining a stiff torso and legs. Avoid any arching (sagging) in your low back, hiking (upwards) in your hips or bending in the knees. Avoid shrugging your shoulder and keep your shoulders positioned directly over your elbows with your palms facing down. Continue to breath while holding this position for a specified time (5+ seconds). While maintaining a stiff torso and extended knees, gently lower your body back towards the mat or floor before relaxing.",
            "views":124 ,
        }
		 "Cobra": {
            "description": "Lie prone (on your stomach) on an exercise mat or floor with your hands by your sides, positioned directly under your shoulders and hands facing forward. Extend your legs and plantar flex your ankles (toes point away from body). ently exhale and press your hips into the mat or floor and pull your chest away from the ground while keeping your hips stable. This will arch your low back and stretch the muscles in your chest and abdominal region. Hold this position for 15 - 30 seconds. Gently relax and lower your upper body to rest back upon the mat or floor. As the length of arms differ, individuals may often lift their hips off the mat or floor as they fully extend their arms. In this case, limit the extension in your arms to keep the hips on the mat.",
            "views": 59,
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
