from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from gregssnorkelscores.models import Location, Spot, UserProfile, Review
from gregssnorkelscores.forms import LocationForm, SpotForm, SearchForm, ReviewForm, UserForm, UserProfileForm
from django.views.generic.detail import DetailView


def home(request):
    context_dict = {}
    context_dict["boldmessage"] = " "

    form = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            spot_title = form.cleaned_data['spot_title']

            try:
                spot = Spot.objects.get(name = spot_title)
            except Spot.DoesNotExist:
                print('This spot does not exist')
            return redirect('/gregssnorkelscores/')
    else:
        form = SearchForm()
        context_dict['form'] = form
    visitor_cookie_handler(request)

    response = render(request, "gregssnorkelscores/home.html", context=context_dict)
    return response


def about(request):
    context_dict = {
        "boldmessage": "This tutorial has been put together by Gregor Johnston"
    }

    visitor_cookie_handler(request)
    context_dict["visits"] = request.session["visits"]

    response = render(request, "gregssnorkelscores/about.html", context=context_dict)
    return response



def SearchSpot(request):

    form = SearchForm()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            spot_title = form.cleaned_data['spot_title']

            try:
                # if it finds the spot it takes you to the spot
                spot = Spot.objects.get(name = spot_title)
                form = SearchForm()
                context = {'form': form,}
                return render(request, 'gregssnorkelscores/spot.html', context)
            except Spot.DoesNotExist:
                print('This spot does not exist')
            return redirect('/gregssnorkelscores/')
    else:
        form = SearchForm()
        context = {'form': form,}
    return render(request, '/gregssnorkelscores/', context)

def aberdeenshire(request):

    location_name = "aberdeenshire"
    location = Location.objects.get(name=location_name)

    spot_list = Spot.objects.filter(location=location).order_by('-reviewsAmount')[:5]

    context_dict = {
        'location': location,
        'spots':spot_list,
        'boldmessage':'All the locations will be displayed in a list here!'
    }

    visitor_cookie_handler(request)

    response = render(request, "gregssnorkelscores/aberdeenshire.html", context=context_dict)
    return response

def moray(request):

    location_name = "moray"
    location = Location.objects.get(name=location_name)

    spot_list = Spot.objects.filter(location=location).order_by('-reviewsAmount')[:5]

    context_dict = {
        'location': location,
        'spots':spot_list,
        'boldmessage':'All the locations will be displayed in a list here!'
    }

    response = render(request, "gregssnorkelscores/moray.html", context=context_dict)
    return response

def westislands(request):

    location_name = "westislands"
    location = Location.objects.get(name=location_name)

    spot_list = Spot.objects.filter(location=location).order_by('-reviewsAmount')[:5]

    context_dict = {
        'location': location,
        'spots':spot_list,
        'boldmessage':'All the locations will be displayed in a list here!'
    }

    visitor_cookie_handler(request)

    response = render(request, "gregssnorkelscores/westislands.html", context=context_dict)
    return response

def highlands(request):
    
    location_name = "highlands"
    location = Location.objects.get(name=location_name)

    spot_list = Spot.objects.filter(location=location).order_by('-reviewsAmount')[:5]

    context_dict = {
        'location': location,
        'spots':spot_list,
        'boldmessage':'All the locations will be displayed in a list here!'
    }

    visitor_cookie_handler(request)

    response = render(request, "gregssnorkelscores/highlands.html", context=context_dict)
    return response

def angus(request):

    location_name = "angus"
    location = Location.objects.get(name=location_name)

    spot_list = Spot.objects.filter(location=location).order_by('-reviewsAmount')[:5]

    context_dict = {
        'location': location,
        'spots':spot_list,
        'boldmessage':'All the locations will be displayed in a list here!'
    }

    visitor_cookie_handler(request)

    response = render(request, "gregssnorkelscores/angus.html", context=context_dict)
    return response

def fife(request):

    location_name = "fife"
    location = Location.objects.get(name=location_name)

    spot_list = Spot.objects.filter(location=location).order_by('-reviewsAmount')[:5]

    context_dict = {
        'location': location,
        'spots':spot_list,
        'boldmessage':'All the locations will be displayed in a list here!'
    }

    visitor_cookie_handler(request)

    response = render(request, "gregssnorkelscores/fife.html", context=context_dict)
    return response
    
def perthking(request):
    
    location_name = "perthking"
    location = Location.objects.get(name=location_name)

    spot_list = Spot.objects.filter(location=location).order_by('-reviewsAmount')[:5]

    context_dict = {
        'location': location,
        'spots':spot_list,
        'boldmessage':'All the locations will be displayed in a list here!'
    }

    visitor_cookie_handler(request)

    response = render(request, "gregssnorkelscores/perthking.html", context=context_dict)
    return response

def stirling(request):
    
    location_name = "stirling"
    location = Location.objects.get(name=location_name)

    spot_list = Spot.objects.filter(location=location).order_by('-reviewsAmount')[:5]

    context_dict = {
        'location': location,
        'spots':spot_list,
        'boldmessage':'All the locations will be displayed in a list here!'
    }

    visitor_cookie_handler(request)

    response = render(request, "gregssnorkelscores/stirling.html", context=context_dict)
    return response

def argyll(request):

    location_name = "argyll"
    location = Location.objects.get(name=location_name)

    spot_list = Spot.objects.filter(location=location).order_by('-reviewsAmount')[:5]

    context_dict = {
        'location': location,
        'spots':spot_list,
        'boldmessage':'All the locations will be displayed in a list here!'
    }

    visitor_cookie_handler(request)

    response = render(request, "gregssnorkelscores/argyll.html", context=context_dict)
    return response

def scotborders(request):

    location_name = "scotborders"
    location = Location.objects.get(name=location_name)

    spot_list = Spot.objects.filter(location=location).order_by('-reviewsAmount')[:5]

    context_dict = {
        'location': location,
        'spots':spot_list,
        'boldmessage':'All the locations will be displayed in a list here!'
    }

    visitor_cookie_handler(request)

    response = render(request, "gregssnorkelscores/scotborders.html", context=context_dict)
    return response

def orkney(request):

    location_name = "orkney"
    location = Location.objects.get(name=location_name)

    spot_list = Spot.objects.filter(location=location).order_by('-reviewsAmount')[:5]

    context_dict = {
        'location': location,
        'spots':spot_list,
        'boldmessage':'All the locations will be displayed in a list here!'
    }

    visitor_cookie_handler(request)

    response = render(request, "gregssnorkelscores/orkney.html", context=context_dict)
    return response

def dumgal(request):

    location_name = "dumgal"
    location = Location.objects.get(name=location_name)

    spot_list = Spot.objects.filter(location=location).order_by('-reviewsAmount')[:5]

    context_dict = {
        'location': location,
        'spots':spot_list,
        'boldmessage':'All the locations will be displayed in a list here!'
    }

    visitor_cookie_handler(request)

    response = render(request, "gregssnorkelscores/dumgal.html", context=context_dict)
    return response

def east(request):
    
    location_name = "east"
    location = Location.objects.get(name=location_name)

    spot_list = Spot.objects.filter(location=location).order_by('-reviewsAmount')[:5]

    context_dict = {
        'location': location,
        'spots':spot_list,
        'boldmessage':'All the locations will be displayed in a list here!'
    }

    visitor_cookie_handler(request)

    response = render(request, "gregssnorkelscores/east.html", context=context_dict)
    return response

def ayr(request):
    
    location_name = "ayr"
    location = Location.objects.get(name=location_name)

    spot_list = Spot.objects.filter(location=location).order_by('-reviewsAmount')[:5]

    context_dict = {
        'location': location,
        'spots':spot_list,
        'boldmessage':'All the locations will be displayed in a list here!'
    }

    visitor_cookie_handler(request)

    response = render(request, "gregssnorkelscores/ayr.html", context=context_dict)
    return response

def show_location(request, location_name_slug):
    context_dict = {}
    spots = Spot.objects.all()
    context_dict['spots'] = spots
    try:
        location = Location.objects.get(slug=location_name_slug)
        spots = Spot.objects.filter(location=location)
        # context_dict['spots'] = spots
        context_dict['location'] = location
    except Location.DoesNotExist:
        context_dict['location'] = None
        # context_dict['spots'] = None 
    return render(request, 'gregssnorkelscores/location.html', context=context_dict)

@login_required
def add_location(request):
    visitor_cookie_handler(request)

    form = LocationForm()
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            loc = form.save(commit=True)
            print(loc, loc.slug)
            return redirect('/gregssnorkelscores/')
        else:
            print(form.errors)

    response = render(request, 'gregssnorkelscores/add_location.html', {'form': form})
    return response

def show_spot(request, location_name_slug, spot_name_slug):
    context_dict = {}

    try:
        location = Location.objects.get(slug=location_name_slug)
        spot = Spot.objects.get(slug=spot_name_slug)
        reviews = Review.objects.filter(spot=spot)
        context_dict['spot'] = spot
        context_dict['reviews'] = reviews

    except (Location.DoesNotExist, Spot.DoesNotExist):
        context_dict['spot'] = None
        context_dict['reviews'] = None
    return render(request, 'gregssnorkelscores/spot.html', context=context_dict)

@login_required
def add_spot(request, location_name_slug):
    visitor_cookie_handler(request)

    location = get_object_or_404(Location, slug=location_name_slug)

    if location is None:
        return redirect('/gregssnorkelscores/')

    form = SpotForm()

    if request.method == 'POST':
        form = SpotForm(request.POST)

        if form.is_valid():
            if location:
                spot = form.save(commit=False)
                spot.location = location
                spot.save()
                return redirect(reverse('gregssnorkelscores:show_location',
                                        kwargs={'location_name_slug':
                                                location_name_slug}))
        else:
            print(form.errors)
    context_dict = {'form': form, 'location': location}
    response = render(request, 'gregssnorkelscores/add_spot.html', context=context_dict)
    return response


def spot(request):
    visitor_cookie_handler(request)

    response = render(request, "gregssnorkelscores/spot.html")
    return response
    

@login_required
def write_review(request, spot_name_slug):
    visitor_cookie_handler(request)
    context = {}

    spot = get_object_or_404(Spot, slug=spot_name_slug)
    context['spot'] = spot

    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            if spot:
                review = form.save(commit=False)
                review.spot = spot
                review.save()
                return redirect(reverse('gregssnorkelscores:after_review',
                                        kwargs={'spot_name_slug':
                                                spot_name_slug}))
    else:
        print(form.errors)
    context['form'] = form
    response = render(request, 'gregssnorkelscores/write_review.html', context)
    return response

@login_required
def after_review(request, spot_name_slug):
    visitor_cookie_handler(request)

    spot = get_object_or_404(Spot, slug=spot_name_slug)

    context = {'spot': spot}
    response = render(request, 'gregssnorkelscores/after_review.html', context)
    return response 

@login_required
def favourites_add(request, id):
    spot = get_object_or_404(Spot, id=id)
    if spot.favourites.filter(id=request.user.id).exists():
        spot.favourites.remove(request.user)
    else:
        spot.favourites.add(request.user)
    response = render(request, "gregssnorkelscores/home.html")
    return response

@login_required
def favourite_list(request):
    new = Spot.newmanager.filter(favourites=request.user)
    return render(request, 'gregssnorkelscores/favourites.html', 
                  {'new': new})

@login_required
def profile(request):
    visitor_cookie_handler(request)

    response = render(request, "gregssnorkelscores/profile.html")
    return response


@login_required
def profile(request):
    visitor_cookie_handler(request)

    response = render(request, "gregssnorkelscores/profile.html")
    return response


def register(request):
    visitor_cookie_handler(request)
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
    context = {'error_message': None}
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
            if User.objects.filter(username=username).exists():
                context['error_message'] = 'Your password is incorrect.'
            else:
                context['error_message'] = 'Your username is incorrect.'

    return render(request, 'gregssnorkelscores/login.html',context)


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse("gregssnorkelscores:home"))

@login_required
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
    visits = int(get_server_side_cookie(request, "visits", "1"))
    last_visit_cookie = get_server_side_cookie(
        request, "last_visit", str(datetime.now())
    )
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], "%Y-%m-%d %H:%M:%S")

    # If it's been more than a day since the last visit...
    if (datetime.now() - last_visit_time).seconds > 0:
        visits = visits + 1
        # Update the last visit cookie now that we have updated the count
        request.session["last_visit"] = str(datetime.now())
    else:
        # Set the last visit cookie
        request.session["last_visit"] = last_visit_cookie

    # Update/set the visits cookie
    request.session["visits"] = visits
