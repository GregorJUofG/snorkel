from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.conf import settings
#from catalog.models import Spots  copied from website idk yet what our equivalent of catalog is


###############
# REVIEWS
# https://michaelstromer.nyc/books/intro-to-django/django-reviews
#################


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


class Spot(models.Model):
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


class Review(models.Model):

    # 1-5 stars
    RATING_CHOICES = (
        (5, '5'),
        (4, '4'),
        (3, '3'),
        (2, '2'),
        (1, '1'),
    )

    spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Publication Date')
    comment = models.TextField(max_length=500)
    value = models.IntegerField(choices=RATING_CHOICES, default=1)

    def __str__(self):
        return '{0}/{1} - {2}'.format(self.book.title, self.user.username, self.value)
    
    class Meta:
        verbose_name = "Spot Review"
        verbose_name_plural = "Spot Reviews" #wont need?
        ordering = ['-pub_date']



# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    
    
    def __str__(self):
        return self.user.username