from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth import authenticate, login as auth_login
from .forms import UserForm, UserProfileForm
from .models import UserProfile


def home(request):
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'

    visitor_cookie_handler(request)

    response = render(request, 'gregssnorkelscores/home.html', context=context_dict)
    return response


def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by Gregor Johnston'}
    
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    response = render(request, 'gregssnorkelscores/about.html', context=context_dict)
    return response

def location(request):
    context_dict = {}
    context_dict['boldmessage'] = 'All the locations will be displayed in a list here!'

    visitor_cookie_handler(request)

    response = render(request, 'gregssnorkelscores/location.html', context=context_dict)
    return response

def add_location(request):
    visitor_cookie_handler(request)

    response = render(request, 'gregssnorkelscores/add_location.html')
    return response

def add_spot(request):
    visitor_cookie_handler(request)

    response = render(request, 'gregssnorkelscores/add_spot.html')
    return response

def spot(request):
    visitor_cookie_handler(request)

    response = render(request, 'gregssnorkelscores/spot.html')
    return response


def write_review(request):
    visitor_cookie_handler(request)

    response = render(request, 'gregssnorkelscores/write_review.html')
    return response

def profile(request):
    visitor_cookie_handler(request)

    response = render(request, 'gregssnorkelscores/profile.html')
    return response

def favourites(request):
    visitor_cookie_handler(request)

    response = render(request, 'gregssnorkelscores/favourites.html')
    return response

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()

            registered = True
            auth_login(request, user)
            return redirect('home')
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'gregssnorkelscores/register.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'registered': registered
    })

def login(request):
    visitor_cookie_handler(request)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate the user.
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return redirect(reverse('home')) 
            else:
                return HttpResponse("Your account is disabled.")
        else:
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'gregssnorkelscores/login.html')
    

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('gregssnorkelscores:home'))

def profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None

    context = {
        'user': request.user,
        'user_profile': user_profile,
    }
    return render(request, 'gregssnorkelscores/profile.html', context)

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request,'last_visit',str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
    '%Y-%m-%d %H:%M:%S')

    # If it's been more than a day since the last visit...
    if (datetime.now() - last_visit_time).seconds > 0:
        visits = visits + 1
        # Update the last visit cookie now that we have updated the count
        request.session['last_visit'] = str(datetime.now())
    else:
        # Set the last visit cookie
        request.session['last_visit'] = last_visit_cookie

    # Update/set the visits cookie
    request.session['visits'] = visits