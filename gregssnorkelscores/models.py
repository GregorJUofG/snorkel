from django.db import models

# Create your models here.
class Location(models.Model):
    # we will want location names to be unique 
    name = models.CharField(max_length=128, unique=True)
    # copied from user model
    picture = models.ImageField(upload_to='location_images', blank=True)
    about = models.CharField(max_length=500)
    favourites = models.IntegerField()
    reviewsAmount = models.IntegerField()
    reviewsAverage = models.FloatField()
    # snorkel spots = ???
    # author = ??


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