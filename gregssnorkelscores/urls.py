from django.urls import path
from gregssnorkelscores import views
from django.contrib.auth.views import LogoutView


app_name = 'gregssnorkelscores'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about,name = 'about'),
    path('add_location/',views.add_location,name = 'add_location'),
    path('location_name/',views.location,name = 'location'),
    path('location_name/add_spot/', views.add_spot, name='add_spot'),
    path('location_name/spot_name/',views.spot, name = 'spot'),
    path('location_name/spot_name/write_review/', views.write_review, name='write_review'),
    path('profile/username/',views.profile,name = 'profile'),
    path('profile/username/favourites/',views.favourites,name = 'favourites'),
    path('fav/<int:id>/',views.favourite_add, name='favourite_add'),
    path('register/',views.register,name = 'register'),
    path('login/',views.login,name = 'login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
