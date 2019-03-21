from django.conf.urls import url
from fitness import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^login/', views.user_login, name='login'),
    url(r'^register/$', views.register, name='register'),

    url(r'^FAQ/$', views.FAQ, name='FAQ'),
    url(r'^about/$', views.about, name='about'),

    url(r'^workout/(?P<workout_name_slug>[\w\-]+)/$',
        views.view_workout, name='view_workout'),
    url(r'^workout/(?P<workout_name_slug>[\w\-]+)/add_exercise/$',
        views.add_exercise, name='add_exercise'),

    url(r'^workouts/$', views.all_workouts, name='workouts'),
    url(r'^my_workouts/$', views.my_workouts, name='my_workouts'),

    url(r'^add_workout/$', views.add_workout, name='add_workout'),
    url(r'^gyms/$', views.nearby_gyms, name='nearby_gyms'),

    url(r'^favourites/$', views.favourites, name='favourites'),
    url(r'^my_account/$', views.my_account, name='my_account'),
    url(r'^logout/$', views.user_logout, name='logout'),

    url(r'^like/$', views.like_workout, name='like_workout'),

    url(r'^favourite/$', views.favourite_workout, name='favourite_workout'),
]
