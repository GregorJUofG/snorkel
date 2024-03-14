import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'snorkel.settings')

import django
django.setup()
from gregssnorkelscores.models import UserProfile, Location, Spot, Review
from datetime import datetime

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
                            'pictures': '',
                            'favourites': 9,
                            'about': 'lots of info here',
                            'reviewAmount':8,
                            'reviewsAverage':4.2, 
                            },
        'South Ayrshire':{'author': 'tashlikessnorkeling',
                          'pictures':'',
                          'favourites': 7,
                          'about': 'infoooo',
                          'reviewsAmount': 8,
                          'reviewsAverage': 3.6,
                         },
    }

    spots = [
        {'name': 'Stonehaven beach',
         'location':'City of Aberdeen',
         'author': 'greglikessnorkeling',
         'pictures': '',
         'postcode': 'AB39 2BD',
         'reviewsAmount': 5,
         # reviews can each be liked individually
         },
         {'name': 'Portlethen',
          'location':'City of Aberdeen',
          'author':'greglikessnorkeling',
          'pictures': '',
          'postcode': 'AB12 4NR',
          'reviewsAmount': 3,
         },
         {'name': 'Ayr beach',
          'location':'South Ayrshire',
          'author': 'tashlikessnorkeling',
          'pictures': '',
          'postcode': 'KA7 4AD',
          'reviewsAmount': 6,
         },
         {'name': 'Prestwick beach',
          'location':'South Ayrshire',
          'author': 'tashlikessnorkeling',
          'pictures': '',
          'postcode': 'KA9 1QL',
          'reviewsAmount': 2,
         },

    ]

    reviews = [
        {'title': 'Amazing beach!',
         'spot': 'stonehaven beach',
         'author': 'greglikessnorkeling',
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
    
def add_location(name, author, pictures, about):
    l = Location.objects.get_or_create(name=name)[0]
    l.author = author
    l.about = about
    l.pictures = pictures
    # when first create location there are no reviews
    l.reviewsAmount = 0 
    l.reviewsAverage = 0
    l.pub_date = datetime.now()
    return l

def add_spot(name, author, pictures, postcode, location):
    s = Spot.objects.get_or_create(name=name)[0]
    s.author = author
    s.location = location
    s.pictures = pictures
    s.postcode = postcode
    s.reviewsAmount = 0
    s.pub_date = datetime.now()
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
    r.pub_date = datetime.now()
    return r

if __name__ == '__main__':
    print('Starting Snorkel population script')
    populate()