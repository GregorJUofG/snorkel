from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse

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
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        # Update the last visit cookie now that we have updated the count
        request.session['last_visit'] = str(datetime.now())
    else:
        # Set the last visit cookie
        request.session['last_visit'] = last_visit_cookie

    # Update/set the visits cookie
    request.session['visits'] = visits