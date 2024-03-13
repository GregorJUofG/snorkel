import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from gregssnorkelscores.models import UserProfile, Location, Spot, Review

def populate():

    # users = [ 
    #     {'name': 'Greg',
    #      'username': 'greglikessnorkeling',
    #      'password': 'foobarbaz',
    #      'profile pic': '',
    #      'experience': 'EXPERT',
    #      'logged in?': False,
    #      'link': 'blah.com',
    #      'favourited spots': ['here']
    #      },
    #     {'name': 'Tash',
    #      'username': 'tashlikessnorkeling',
    #      'other info':'info'
    #      }
    # ]

    locations = {
        'City of Aberdeen':{'author': 'greglikessnorkeling',
                            'pictures': '','favourites': 9,
                            'about': 'lots of info here',
                            'reviewAmount':5,
                            'reviewsAverage':4, 
                            'pub_date': '12/06/22',
                            },
        'South Ayrshire':{'author': 'tashlikessnorkeling' 
                         },
    }

    spots = [
        {'name': 'stonehaven beach',
         'location':'City of Aberdeen',
         'author': 'greglikessnorkeling',
         'pictures': '',
         'postcode': 'AB39 2BD',
         'reviewsAmount': 5,
         'pub_date': '12/06/22',
         # reviews can each be liked individually
         }
    ]

    reviews = [
        {'title': 'Amazing beach!',
         'spot': 'stonehaven beach',
         'author': 'greglikessnorkeling',
         'pub_date': '12/06/22',
         'comment': 'really nice place to snorkel :)',
         'rating': 5,
         'likes':7,
         }
    ]

    # go through location and add each spot
    for loc, loc_data in locations.items():
        l = add_location(loc)
        for sList in loc_data['snorkel spots']: # s is a list of snorkel spots
            for spot in sList: # each spot in the spot list
                add_spot(spot)


# some functions
    
def add_location(name, author, picture, about):
    l = Location.objects.get_or_create(name=name)[0]
    l.author = author
    l.about = about
    l.pictures = picture
    # when first create location there are no reviews
    l.reviewsAmount = 0 
    l.reviewsAverage = 0
    return l

def add_spot(name, author, picture, postcode, location):
    s = Spot.objects.get_or_create(name=name)[0]
    s.author = author
    s.location = location
    s.picture = picture
    s.postcode = postcode
    s.reviewsAmount = 0
    # pub date will set itself?
    return s

def add_review(title, spot, author, comment, value):
    r = Review.objects.get_or_create(title=title)[0]
    r.author = author
    r.spot = spot
    r.comment = comment
    r.value = value
    r.spot.reviewsAmount += 1
    r.spot.location.reviewsAmount += 1
    r.spot.location.reviewsAverage = ((r.spot.location.reviewsAverage*r.spot.location.reviewsAmount)+r.value)/r.spot.location.reviewsAmount
    return r

if __name__ == '__main__':
    print('Starting Snorkel population script')
    populate()