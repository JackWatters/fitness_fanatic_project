from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("This is the welcome page <a href='/fitness_fanatics/about/'>About us</a>")

def login(request):
    return HttpResponse("This is the login page")

def FAQ(request):
    return HttpResponse("This is the FAQ page")

def about(request):
    return HttpResponse("This is the about us page <a href='/fitness_fanatics/'>Home</a>")
    
def register(request):
    return HttpResponse("This is the register page")


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
