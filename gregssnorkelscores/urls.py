from django.urls import path
from gregssnorkelscores import views

app_name = 'gregssnorkelscores'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/',views.about,name = 'about'),
]
