from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from gregssnorkelscores.models import Location, Spot, UserProfile, Review
from gregssnorkelscores.form import LocationForm, SpotForm, SearchForm, ReviewForm


def home(request):
    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'

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

    response = render(request, 'gregssnorkelscores/home.html', context=context_dict)
    return response


def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by Gregor Johnston'}
    
    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

    response = render(request, 'gregssnorkelscores/about.html', context=context_dict)
    return response


def SearchSpot(request):

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
        context = {'form': form,}
    return render(request, '/gregssnorkelscores/', context)



def location(request):
    spot_list = Spot.objects.order_by('-reviewsAmount')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'All the locations will be displayed in a list here!'
    context_dict['spots'] = spot_list

    visitor_cookie_handler(request)

    response = render(request, 'gregssnorkelscores/location.html', context=context_dict)
    return response

def show_location(request, location_name_slug):
    context_dict = {}
    try:
        location = Location.objects.get(slug=location_name_slug)
        spots = Spot.objects.filter(location=location)
        context_dict['spots'] = spots
        context_dict['location'] = location
    except Location.DoesNotExist:
        context_dict['location'] = None
        context_dict['spots'] = None 
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


def show_spot(request, spot_name_slug):
    context_dict = {}

    try:
        spot = Spot.objects.get(slug=spot_name_slug)
        reviews = Review.objects.filter(spot=spot)
        context_dict['spot'] = spot
        context_dict['reviews'] = reviews

    except Spot.DoesNotExist:
        context_dict['spot'] = None
        context_dict['reviews'] = None
    return render(request, 'gregssnorkelscores/spot.html', context=context_dict)

@login_required
def add_spot(request):
    visitor_cookie_handler(request)

    try:
        location = Location.ojects.get(slug=location_name_slug)
    except Location.DoesNotExist:
        location = None

    if location is None:
        return redirect('/gregssnorkelscores/')
    
    form = SpotForm()

    if request.method == 'POST':
        form = SpotForm(request.POST)

        if form.is_valid():
            if location:
                spot = form.save(commit=False)
                spot.location = location
                # other variables for spot

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

    response = render(request, 'gregssnorkelscores/spot.html')
    return response

@login_required
def write_review(request):
    visitor_cookie_handler(request)

    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Your review has been taken')
    else:
        form = ReviewForm()
        context = {'form': form,}
    response = render(request, 'gregssnorkelscores/write_review.html', context)
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
    
    visitor_cookie_handler(request)

    response = render(request, 'gregssnorkelscores/register.html')
    return response

    # HONGHUI's task

    # # A boolean value for telling the template
    # # whether the registration was successful.
    # # Set to False initially. Code changes value to
    # # True when registration succeeds.
    # registered = False
    # # If it's a HTTP POST, we're interested in processing form data.
    # if request.method == 'POST':
    #     # Attempt to grab information from the raw form information.
    #     # Note that we make use of both UserForm and UserProfileForm.
    #     user_form = UserForm(request.POST)
    #     profile_form = UserProfileForm(request.POST)

    #     # If the two forms are valid...
    #     if user_form.is_valid() and profile_form.is_valid():
    #         # Save the user's form data to the database.
    #         user = user_form.save()

    #         # Now we hash the password with the set_password method.
    #         # Once hashed, we can update the user object.
    #         user.set_password(user.password)
    #         user.save()

    #         # Now sort out the UserProfile instance.
    #         # Since we need to set the user attribute ourselves,
    #         # we set commit=False. This delays saving the model
    #         # until we're ready to avoid integrity problems.
    #         profile = profile_form.save(commit=False)
    #         profile.user = user

    #         # Did the user provide a profile picture?
    #         # If so, we need to get it from the input form and
    #         #put it in the UserProfile model.
    #         if 'picture' in request.FILES:
    #             profile.picture = request.FILES['picture']

    #         # Now we save the UserProfile model instance.
    #         profile.save()

    #         # Update our variable to indicate that the template
    #         # registration was successful.
    #         registered = True
    #     else:
    #         # Invalid form or forms - mistakes or something else?
    #         # Print problems to the terminal.
    #         print(user_form.errors, profile_form.errors)
    # else:
    #     # Not a HTTP POST, so we render our form using two ModelForm instances.
    #     # These forms will be blank, ready for user input.
    #     user_form = UserForm()
    #     profile_form = UserProfileForm()

    # # Render the template depending on the context.
    # return render(request,
    #               'gregssnorkelscores/register.html',
    #               context = {'user_form': user_form,
    #                          'profile_form': profile_form,
    #                          'registered': registered})

def login(request):

    visitor_cookie_handler(request)

    response = render(request, 'gregssnorkelscores/login.html')
    return response
    # HONGHUI's task

    # # If the request is a HTTP POST, try to pull out the relevant information.
    # if request.method == 'POST':
    #     # Gather the username and password provided by the user.
    #     # This information is obtained from the login form.
    #     # We use request.POST.get('<variable>') as opposed
    #     # to request.POST['<variable>'], because the
    #     # request.POST.get('<variable>') returns None if the
    #     # value does not exist, while request.POST['<variable>']
    #     # will raise a KeyError exception.
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
    #     # Use Django's machinery to attempt to see if the username/password
    #     # combination is valid - a User object is returned if it is.
    #     user = authenticate(username=username, password=password)
    #     # If we have a User object, the details are correct.
    #     # If None (Python's way of representing the absence of a value), no user
    #     # with matching credentials was found.
    #     if user:
    #         # Is the account active? It could have been disabled.
    #         if user.is_active:
    #             # If the account is valid and active, we can log the user in.
    #             # We'll send the user back to the homepage.
    #             login(request, user)
    #             return redirect(reverse('gregssnorkelscores:home'))
    #         else:
    #             # An inactive account was used - no logging in!
    #             return HttpResponse("Your Rango account is disabled.")
    #     else:
    #         # Bad login details were provided. So we can't log the user in.
    #         print(f"Invalid login details: {username}, {password}")
    #         return HttpResponse("Invalid login details supplied.")
    # # The request is not a HTTP POST, so display the login form.
    # # This scenario would most likely be a HTTP GET.
    # else:
    #     # No context variables to pass to the template system, hence the
    #     # blank dictionary object...
    #     return render(request, 'gregssnorkelscores/login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('gregssnorkelscores:home'))

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