import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'snorkel.settings')

import django
django.setup()
from gregssnorkelscores.models import UserProfile, Location, Spot, Review
from datetime import datetime

def populate():

    aberdeenshire_spots = {
        'Stonehaven beach':{'author': 'greglikessnorkeling',
                            'pictures': '',
                            'favourites': 5,
                            'postcode': 'AB39 2BD',
                            'reviewsAmount': 2,     # reviews can each be liked individually
                            'reviews':{
                                'Amazing beach!':{
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
                            'reviews':{
                                'Good beach!':{
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
        'aberdeenshire':{   'pictures': '',
                            'about': 'The granite city, Aberdeen!',
                            'reviewsAmount':8,
                            'reviewsAverage':4.2,
                            'spots':aberdeenshire_spots
                        },
        'south_ayrshire':{'pictures':'',
                          'about': 'infoooo',
                          'reviewsAmount': 8,
                          'reviewsAverage': 3.6,
                          'spots':ayr_spots
                        },
    }
    
    # Don't think it is necessary to populate users...
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

    # go through location and add each spot
    for loc, loc_data in locations.items():
        l = add_location(loc,
                         loc_data['pictures'],loc_data['about'],
                         loc_data['reviewsAmount'],loc_data['reviewsAverage']
                         )
        
        for spot, spot_data in loc_data['spots'].items():
            s = add_spot(spot,l,
                     spot_data['author'],spot_data['pictures'],
                     spot_data['postcode'],spot_data['reviewsAmount']
                     )
            
            for review, rev_data in spot_data['reviews'].items():
                add_review(review, s,
                           rev_data['author'],rev_data['comment'],
                           rev_data['comment'],rev_data['rating'],
                           rev_data['likes']
                           )
    
def add_location(name, pictures, about, reviewsAmount, reviewsAverage):
    l = Location.objects.get_or_create(name=name)[0]
    l.pictures = pictures
    l.about = about
    l.reviewsAmount = reviewsAmount
    l.reviewsAverage = reviewsAverage
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
    # Some fancy code I will add back later
    # r.spot.reviewsAmount += 1
    # r.spot.location.reviewsAmount += 1
    # r.spot.location.reviewsAverage = ((r.spot.location.reviewsAverage*r.spot.location.reviewsAmount)+r.rating)/r.spot.location.reviewsAmount
    r.pub_date = datetime.now()
    r.save()
    return r

if __name__ == '__main__':
    print('Starting Snorkel population script')
    populate()