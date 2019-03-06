from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from fitness.forms import UserForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from fitness.models import Workout,Exercise
from fitness.forms import WorkoutForm, UserForm


# Create your views here.

def index(request):
    workout_list = Workout.objects.order_by('-views')[:3]
    return render(request, 'fitness/index.html', context={'workouts': workout_list})

def user_login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                 return HttpResponse("Your Fitness fanatic account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'fitness/login.html',{})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index')) 

def FAQ(request):
    #return HttpResponse("This is the FAQ page")
    return render(request, 'fitness/base.html', context={})

def about(request):
    #return HttpResponse("This is the about us page <a href='/fitness_fanatics/'>Home</a>")
    return render(request, 'fitness/about.html', context={})

def register(request):
    
    registered = False

    if request.method == 'POST':

        user_form = UserForm(data=request.POST) 
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            
            profile.save()

            registered = True
            
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    
    return render(request,'fitness/register.html',
                {'user_form': user_form,
                'profile_form': profile_form,
                'registered': registered})

def view_workout(request, workout_name_slug):
    context_dict = {}

    try:
        workout = Workout.objects.get(slug = workout_name_slug)
        excercises = Excercise.objects.filter(workout = workout)

        context_dict['excercises'] = excercises
        context_dict['workout'] = workout
    except Workout.DoesNotExist:
        context_dict['excercises'] = None
        context_dict['workout'] = None

    return render(request, 'rango/category.html', context_dict)

@login_required          
def favourites(request):
    return HttpResponse("This is the favourites page")

def all_workouts(request):
    return HttpResponse("This is the workouts page")

@login_required  
def my_workouts(request):
    return HttpResponse("This is the my workouts page")

@login_required  
def add_workout(request):
    form = WorkoutForm()

    if request.method == 'POST':
        form = WorkoutForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)
    
    return render(request, 'fitness/add_workout.html', context={})

@login_required  
def add_excercise(request,workout_name_slug):
    form = ExerciseForm

    form = ExerciseForm()
    if request.method == 'POST':
        form = ExerciseForm(reuqest.POST)
        if form.is_valid():
            page = form.save(commit=False)
            page.views = 0
            page.save()
            return show_workout(request, workout_name_slug)
        else:
            print(form.erros)

    context_dict = {'form':form, 'category': category}
    return render(request, 'rango/add_page.html', context_dict)

@login_required  
def my_account(request):
    return HttpResponse("This is the my account page")
