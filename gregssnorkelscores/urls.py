from django.urls import path
from gregssnorkelscores import views

app_name = 'gregssnorkelscores'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about,name = 'about'),
    path('location_name/',views.location,name = 'location'),
    path('location_name/write_review/', views.write_review, name='write_review'),
    path('profile/username/',views.profile,name = 'profile'),
    path('add_location/',views.add_location,name = 'add_location'),
    path('register/',views.register,name = 'register'),
    path('login/',views.login,name = 'login'),
]
