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

    aberdeen_spots = {'Stonehaven beach':{
                            'location':'City of Aberdeen',
                            'author': 'greglikessnorkeling',
                            'spotAbout':'stuff',
                            'pictures': '',
                            'favourites': 5,
                            'postcode': 'AB39 2BD',
                            'reviewsAmount': 2,     # reviews can each be liked individually
                            'reviews':{'Amazing beach!':{
                                            'author': 'greglikessnorkeling',
                                            # comment = what the review is
                                            'comment': 'really nice place to snorkel :)',
                                            'rating': 5, # (Stars)
                                            'likes':7
                                        },
                                        'Great Beach!':{
                                            'author': 'tashlovessnorkelling',
                                            'comment': 'Saw a seal!',
                                            'rating': 4,
                                            'likes':18
                                        }
                                    }
                            },
                        'Portlethen Beach':{
                            'location':'City of Aberdeen',
                            'author':'greglikessnorkeling',
                            'spotAbout':'stuff',
                            'pictures': '',
                            'favourites': 8,
                            'postcode': 'AB12 4NR',
                            'reviewsAmount': 1,
                            'reviews':{'Good beach!':{
                                        'author': 'greglikessnorkeling',
                                        # comment = what the review is
                                        'comment': 'really nice place to snorkel :)',
                                        'rating': 5, # (Stars)
                                        'likes':7
                                        }
                                    }
                                }
                            }

    ayr_spots = {
        'Ayr beach':{
            'location':'South Ayrshire',
            'author':'greglikessnorkeling',
            'spotAbout':'stuff',
            'pictures': '',
            'favourites': 4,
            'postcode': 'AB12 4NR',
            'reviewsAmount': 1,
            'reviews':{'Good beach!':{
                        'author': 'greglikessnorkeling',
                        # comment = what the review is
                        'comment': 'really nice place to snorkel :)',
                        'rating': 5, # (Stars)
                        'likes':7
                        }
                    }
                }
            }
    

    locations = {
        'City of Aberdeen':{'author': 'greglikessnorkeling',
                            'pictures': '',
                            #'about': 'lots of info here',
                            #'reviewAmount':8,
                            #'reviewsAverage':4.2,
                            'spots':aberdeen_spots
                            },
        'South Ayrshire':{'author': 'tashlikessnorkeling',
                          'pictures':'',
                          #'about': 'infoooo',
                          #'reviewsAmount': 8,
                          #'reviewsAverage': 3.6,
                          'spots':ayr_spots
                         },
    }


    # go through location and add each spot
    for loc, loc_data in locations.items():
        l = add_location(loc,loc_data['author'],loc_data['pictures'],)
        
        for spot, spot_data in loc_data['spots'].items():
            # variables
            numOfReviews=0
            reviewtotal=0 # used for average
            
            #making reviews first so we can use the data in spot
            for review, rev_data in spot_data['reviews']:
                # for each review update variables
                numOfReviews += 1
                reviewtotal+=rev_data['rating']
                add_review(review, s,
                           rev_data['author'],rev_data['comment'],
                           rev_data['comment'],rev_data['rating'],
                           rev_data['likes']
                           )
            # after gone through all reviews then adjust spot values
            s = add_spot(spot,l,
                     spot_data['author'],spot_data['pictures'],
                     spot_data['favourites'],spot_data['postcode'],
                     spot_data['spotAbout'],spot_data['reviewsAmount']
                     )


# some functions
    
def add_location(name, author, pictures):
    l = Location.objects.get_or_create(name=name)[0]
    l.author = author
    l.pictures = pictures
    l.pub_date = datetime.now()
    l.save()
    return l

def add_spot(name, location, author, spotAbout, pictures, favourites, postcode, reviewsAmount):
    s = Spot.objects.get_or_create(name=name, location=location)[0]
    s.author = author
    s.spotAbout = spotAbout
    s.pictures = pictures
    s.favourites = favourites
    s.postcode = postcode
    s.reviewsAmount = reviewsAmount
    s.pub_date = datetime.now()
    s.save()
    return s

def add_review(title, spot, author, comment, rating, likes):
    r = Review.objects.get_or_create(title=title)[0]
    r.spot = spot
    r.author = author
    r.comment = comment
    r.rating = rating
    r.likes = likes
    # r.spot.reviewsAmount += 1
    # r.spot.location.reviewsAmount += 1
    # r.spot.location.reviewsAverage = ((r.spot.location.reviewsAverage*r.spot.location.reviewsAmount)+r.rating)/r.spot.location.reviewsAmount
    r.pub_date = datetime.now()
    return r

if __name__ == '__main__':
    print('Starting Snorkel population script')
    populate()