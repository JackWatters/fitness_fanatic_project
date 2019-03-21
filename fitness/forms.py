from django import forms
from django.contrib.auth.models import User
from fitness.models import Workout, Exercise, UserProfile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username','email','password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture','favourites',)

class WorkoutForm(forms.ModelForm):

    title = forms.CharField(max_length=Workout.length_max,
                           help_text = "Please name your workout.")
    description = forms.CharField(widget=forms.Textarea, max_length=280,
                                  help_text = "Please describe your workout.")
    image = forms.ImageField(required=False)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    author = forms.IntegerField(widget=forms.HiddenInput(), required = False)
    class Meta:
        model = Workout
        fields = ('title','description','image','views','author')
