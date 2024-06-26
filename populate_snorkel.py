import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'snorkel.settings')

import django
django.setup()

# Import the User model and other models
from django.contrib.auth.models import User
from gregssnorkelscores.models import UserProfile, Location, Spot, Review


def populate():

    aberdeenshire_spots = {
                        'Stonehaven beach':{
                            'location':'City of Aberdeen',
                            'author': 'greglikessnorkeling',
                            'spotAbout': 'words',
                            'pictures': '',
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
    angus_spots = {}
    argyll_spots = {}
    
    ayr_spots = {
        'Ayr beach':{
            'location':'South Ayrhsire',
            'author':'greglikessnorkeling',
            'spotAbout':'stuff',
            'pictures': '',
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
    
    dum_spots = {}
    east_spots = {}
    fife_spots = {}
    high_spots = {}
    mor_spots = {}
    ork_spots = {}
    per_spots = {}
    scot_spots = {}
    stir_spots = {}
    west_spots = {}

    locations = {
        'aberdeenshire':{   'pictures': '',
                            'about': 'The granite city, Aberdeen!',
                            'reviewsAmount':8,
                            'reviewsAverage':4.2,
                            'spots':aberdeenshire_spots
                        },
        'angus':{   'pictures': '',
                            'about': 'snorkel',
                            'reviewsAmount':3,
                            'reviewsAverage':3.2,
                            'spots':angus_spots
                        },
        'argyll':{   'pictures': '',
                            'about': 'snorkel',
                            'reviewsAmount':4,
                            'reviewsAverage':2.9,
                            'spots':argyll_spots
                        },
        'ayr':{'pictures':'',
                          'about': 'infoooo',
                          'reviewsAmount': 8,
                          'reviewsAverage': 3.6,
                          'spots':ayr_spots
                        },
        'dumgal':{   'pictures': '',
                            'about': 'snorkel',
                            'reviewsAmount':5,
                            'reviewsAverage':4.1,
                            'spots':dum_spots
                        },
        'east':{   'pictures': '',
                            'about': 'smnorkel',
                            'reviewsAmount':10,
                            'reviewsAverage':3.6,
                            'spots':east_spots
                        },
        'fife':{   'pictures': '',
                            'about': 'snirkel',
                            'reviewsAmount':0,
                            'reviewsAverage':1,
                            'spots':fife_spots
                        },
        'highlands':{   'pictures': '',
                            'about': 'snkorkel',
                            'reviewsAmount':12,
                            'reviewsAverage':4.8,
                            'spots':high_spots
                        },
        'moray':{   'pictures': '',
                            'about': 'snorkel',
                            'reviewsAmount':7,
                            'reviewsAverage':4.5,
                            'spots':mor_spots
                        },
        'orkney':{   'pictures': '',
                            'about': 'snorkel',
                            'reviewsAmount':6,
                            'reviewsAverage':2.9,
                            'spots':ork_spots
                        },
        'perthking':{   'pictures': '',
                            'about': 'snorkel',
                            'reviewsAmount':10,
                            'reviewsAverage':4.3,
                            'spots':per_spots
                        },
        'scotborders':{   'pictures': '',
                            'about': 'snorkel',
                            'reviewsAmount':8,
                            'reviewsAverage':3.8,
                            'spots':scot_spots
                        },
        'stirling':{   'pictures': '',
                            'about': 'snokrel',
                            'reviewsAmount':6,
                            'reviewsAverage':2.5,
                            'spots':stir_spots
                        },
        'westislands':{   'pictures': '',
                            'about': 'snorkel',
                            'reviewsAmount':7,
                            'reviewsAverage':3.2,
                            'spots':west_spots
                        },
    }

    # go through location and add each spot
    for loc, loc_data in locations.items():
        l = add_location(loc,
                         loc_data['pictures'],loc_data['about'],
                         loc_data['reviewsAmount'],loc_data['reviewsAverage']
                         )
        
        for spot, spot_data in loc_data['spots'].items():
            s = add_spot(spot,l,spot_data['author'],spot_data['spotAbout'],spot_data['pictures'],spot_data['reviewsAmount'],)
            
            for review, rev_data in spot_data['reviews'].items():
                add_review(review, s,
                           rev_data['author'],rev_data['comment'],
                           rev_data['rating'],rev_data['likes']
                           )
    
def add_location(name, pictures, about, reviewsAmount, reviewsAverage):
    l = Location.objects.get_or_create(name=name)[0]
    l.pictures = pictures
    l.about = about
    l.reviewsAmount = reviewsAmount
    l.reviewsAverage = reviewsAverage
    l.save()
    return l

def add_spot(name, location, author, spotAbout, pictures, reviewsAmount):
    s = Spot.objects.get_or_create(name=name, location=location)[0]
    s.author = author
    s.spotAbout = spotAbout
    s.pictures = pictures
    s.reviewsAmount = reviewsAmount
    s.save()
    return s

def add_review(title, spot, author_username, comment, rating, likes):
    # Fetch or create the User instance
    author, created = User.objects.get_or_create(username=author_username)
    
    # Now when creating the Review, we provide the User instance for the author field
    r, created = Review.objects.get_or_create(
        title=title, 
        defaults={
            'spot': spot,
            'author': author,  # Here, we use the User instance
            'comment': comment,
            'rating': rating,
            'likes': likes
        }
    )
    if not created:
        r.comment = comment
        r.rating = rating
        r.likes = likes
        r.save()

    return r

if __name__ == '__main__':
    print('Starting Snorkel population script')
    populate()