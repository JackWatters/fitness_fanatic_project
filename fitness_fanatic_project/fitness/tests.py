from django.test import TestCase
from fitness.models import Workout
from django.core.urlresolvers import reverse

# Create your tests here.
class WorkoutMethodTests(TestCase):
    def test_slug_line_creation(self):
        testWorkout = Workout.objects.create(title="Random Title String")
        testWorkout.save()
        self.assertEqual(testWorkout.slug, 'random-title-string')

class IndexViewTests(TestCase):
    def test_index_view_with_no_workouts(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No Workouts Have Been Uploaded :(")
        self.assertQuerysetEqual(response.context['workouts'], [])
    
    def test_added_workout_appears_on_homescreen(self):
        testWorkout = Workout.objects.create(title="Random Title String")
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Random Title String")

    def test_no_more_than_three_cards_appear_on_homescreen(self):
        testWorkout = Workout.objects.create(title="workout1")
        testWorkout = Workout.objects.create(title="workout2")
        testWorkout = Workout.objects.create(title="workout3")
        testWorkout = Workout.objects.create(title="workout4")
        
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "workout4")
    
    def test_three_cards_appear_on_homescreen(self):
        testWorkout = Workout.objects.create(title="workout1")
        testWorkout = Workout.objects.create(title="workout2")
        testWorkout = Workout.objects.create(title="workout3")
        
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "workout1")
        self.assertContains(response, "workout2")
        self.assertContains(response, "workout3")

    def test_login_link(self):
        response = self.client.get(reverse("index"))
        self.assertContains(response, '<a class="nav-link" href ="%s">' % reverse("login"))