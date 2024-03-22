from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = 'gregssnorkelscores'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about,name = 'about'),
    path('add_location/',views.add_location,name = 'add_location'),
    path('aberdeenshire/',views.aberdeenshire,name = 'aberdeenshire'),
    path('moray/',views.moray,name = 'moray'),
    path('westislands/',views.westislands,name = 'westislands'),
    path('east/',views.east,name = 'east'),
    path('fife/',views.fife,name = 'fife'),
    path('stirling/',views.stirling,name = 'stirling'),
    path('orkney/',views.orkney,name = 'orkney'),
    path('perthking/',views.perthking,name = 'perthking'),
    path('highlands/',views.highlands,name = 'highlands'),
    path('scotborders/',views.scotborders,name = 'scotborders'),
    path('dumgal/',views.dumgal,name = 'dumgal'),
    path('ayr/',views.ayr,name = 'ayr'),
    path('argyll/',views.argyll,name = 'argyll'),
    path('angus/',views.angus,name = 'angus'),
    path('register/',views.register,name = 'register'),
    path('login/',views.login,name = 'login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('<slug:spot_name_slug>/write_review/', views.write_review, name='write_review'),
    path('<slug:spot_name_slug>/after_review/', views.after_review, name='after_review'),
    path('profile/username/',views.profile,name = 'profile'),
    path('<slug:location_name_slug>/',views.show_location,name='show_location'),
    path('<slug:location_name_slug>/add_spot/', views.add_spot, name='add_spot'),
    path('<slug:location_name_slug>/<slug:spot_name_slug>/',views.show_spot,name = 'show_spot'),
]
