from django.urls import path
from gregssnorkelscores import views
from django.contrib.auth.views import LogoutView


app_name = 'gregssnorkelscores'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about,name = 'about'),
    path('add_location/',views.add_location,name = 'add_location'),
    path('aberdeenShire',views.aberdeenShire,name = 'aberdeenShire'),
    path('moray',views.moray,name = 'moray'),
    path('westIslands',views.westIslands,name = 'westIslands'),
    path('east',views.east,name = 'east'),
    path('fife',views.fife,name = 'fife'),
    path('stirling',views.stirling,name = 'stirling'),
    path('orkney',views.orkney,name = 'orkney'),
    path('perthKing',views.perthKing,name = 'perthKing'),
    path('highlands',views.highlands,name = 'highlands'),
    path('scotBorders',views.scotBorders,name = 'scotBorders'),
    path('dumGal',views.dumGal,name = 'dumGal'),
    path('ayr',views.ayr,name = 'ayr'),
    path('argyll',views.argyll,name = 'argyll'),
    path('angus',views.angus,name = 'angus'),
    path('register/',views.register,name = 'register'),
    path('login/',views.login,name = 'login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),
    path('<slug:spot_name_slug>/write_review/', views.write_review, name='write_review'),
    path('profile/username/',views.profile,name = 'profile'),
    path('<slug:location_name_slug>/',views.show_location,name='show_location'),
    path('<slug:location_name_slug>/add_spot/', views.add_spot, name='add_spot'),
    # path('orkney/add_spot/', views.add_spot, name='add_spot'),
    path('<slug:location_name_slug>/<slug:spot_name_slug>/',views.show_spot,name = 'show_spot'),
]

#     path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
#  <a href="/rango/category/{{ category.slug }}/add_page/">Add Page</a> <br />
