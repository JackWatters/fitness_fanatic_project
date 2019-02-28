from django.conf.urls import url
from fitness import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/', views.user_login, name='login'),
    url(r'^FAQ/', views.FAQ, name='FAQ'),
    url(r'^about/', views.about, name='about'),
    url(r'^register/', views.register, name='register'),
    url(r'^view_post/', views.view_post, name='view post'),
    url(r'^favourites/', views.favourites, name='favourites'),
    url(r'^workouts/', views.workouts, name='workouts'),
    url(r'^my_workouts/', views.my_workouts, name='my workouts'),
    url(r'^add_workout/', views.add_workout, name='add workout'),
    url(r'^my_account/', views.my_account, name='my_account'),
    url(r'^logout/$', views.user_logout, name='logout'),
    
]

