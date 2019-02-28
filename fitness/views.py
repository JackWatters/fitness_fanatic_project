from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse("This is the welcome page <a href='/fitness_fanatics/about/'>About us</a>")
    return render(request, 'fitness/index.html', context={})

def login(request):
    #return HttpResponse("This is the login page")

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                 return HttpResponse("Your Fitness fanatic account is disabled.")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'fitness/login.html',{})

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

def view_post(request):
    return HttpResponse("This is the view post page")

def favourites(request):
    return HttpResponse("This is the favourites page")

def workouts(request):
    return HttpResponse("This is the workouts page")

def my_workouts(request):
    return HttpResponse("This is the my workouts page")

def add_workout(request):
    return HttpResponse("This is the add workout page")

def my_account(request):
    return HttpResponse("This is the my account page")
