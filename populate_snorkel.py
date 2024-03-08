import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from gregssnorkelscores.models import UserProfile, Location, Spots
import Experience


#######################
### WEBSITE FOR REVIEWS???
### https://django-rated-reviews.readthedocs.io/en/latest/quickstart.html
#######################

def populate():

    users = [ 
        {'name': 'Greg',
         'username': 'greglikessnorkeling',
         'password': 'foobarbaz',
         'profile pic': '',
         'experience': Experience.EXPERT,
         'logged in?': False,
         'link': 'blah.com',
         'places created': ['here', 'there', 'everywhere'],
         'favourited places': ['here']
         },
        {'name': 'Tash',
         'username': 'tashlikessnorkeling',
         'other info':'info'
         }
    ]

    locations = {
        'City of Aberdeen':{'author': 'greglikessnorkeling',
                            'pictures': '','favourites': 9,
                            'about': 'lots of info here',
                            'total reviews': [5, 1.6], 
                            #num of reviews and average rating from them
                            'snorkel spots': ['place', 'other place'],
                            },
        'South Ayrshire':{'author': 'tashlikessnorkeling' 
                         },
    }

    spots = [
        {'name': 'stonehaven beach',
         'author': 'greglikessnorkeling',
         'pictures': '',
         'postcode': 'AB39 2BD',
         'reviews num': 5,
         'reviews':{'words':2, 'different words':1}
         # reviews can each be liked individually
         }
    ]

    # go through location and add each spot
    for loc, loc_data in locations.items():
        l = add_location(loc)
        for sList in loc_data['snorkel spots']: # s is a list of snorkel spots
            for spot in sList: # each spot in the spot list
                #### idk how to do this
                add_spot(spot)


# some functions
    
def add_location(name, author, picture, about):
    l = Location.objects.get_or_create(name=name)[0]
    l.author = author
    l.about = about
    l.picture = picture
    # when first create location there are no reviews
    l.reviewsAmount = 0 
    l.reviewsAverage = 0
    return l

def add_spot(name, author, picture, postcode, location):
    s = Spots.objects.get_or_create(name=name)[0]
    s.author = author
    s.location = location
    s.picture = picture
    s.postcode = postcode
    s.reviewsAmount = 0
    s.reviews = []
    return s

def add_review(rating, author, dateTime, content):
    ## later 
    return

if __name__ == '__main__':
    print('Starting Snorkel population script')
    populate()