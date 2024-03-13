from django.db import models

class Location(models.Model):
    NAME_MAX_LENGTH = 128
    # we will want location names to be unique 
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=True)
    # copied from user model
    creator = models.CharField(max_length = NAME_MAX_LENGTH)
    pictures = models.ImageField(upload_to='location_images', blank=True)
    about = models.CharField(max_length=1000)
    favourites = models.IntegerField()
    reviewsAmount = models.IntegerField()
    reviewsAverage = models.FloatField()
    #NOT SURE ABOUT THIS ONE?
    snorkelSpots = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class Spots(models.Model):
    ## think this is right
    ## cpoied how category and page are connected
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    # will also want names here to be unique
    name = models.CharField(max_length=128, unique=True)
    # copied from django
    url = models.URLField()
    # copied from user model
    picture = models.ImageField(upload_to='spot_images', blank=True)
    postcode = models.CharField(max_length=8)
    reviewsAmount = models.IntegerField()
    # reviews = ??
    # author = ??

# class UserProfile(models.Model):
#     # This line is required. Links UserProfile to a User model instance. 
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     # The additional attributes we wish to include.
#     website = models.URLField(blank=True)
#     picture = models.ImageField(upload_to='profile_images', blank=True)
#     def __str__(self):
#         return self.user.username
