from django.urls import path
from gregssnorkelscores import views
from django.contrib.auth.views import LogoutView


app_name = 'gregssnorkelscores'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about,name = 'about'),
    path('location/',views.location,name = 'location'),
    path('add_spot/', views.add_spot, name='add_spot'), # dont know location till we add spot so it doessnt get it in the url
    path('spot/',views.show_spot, name = 'show_spot'), # getting rid of location_name rn
    path('spot/<slug:spot_name_slug>/write_review/', views.write_review, name='write_review'),
    path('profile/username/',views.profile,name = 'profile'),
    path('profile/username/favourites/',views.favourites,name = 'favourites'),
    path('fav/<int:id>/',views.favourite_add, name='favourite_add'),
    path('register/',views.register,name = 'register'),
    path('login/',views.login,name = 'login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
]
