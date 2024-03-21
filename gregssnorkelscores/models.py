from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.conf import settings

# from catalog.models import Spots  copied from website idk yet what our equivalent of catalog is

###############
# REVIEWS
# https://michaelstromer.nyc/books/intro-to-django/django-reviews
#################


class Location(models.Model):
    NAME_MAX_LENGTH = 128

    name = models.CharField(max_length=128, unique=True) # (We will want location names to be unique)
    pictures = models.ImageField(upload_to="location_images", blank=True)
    about = models.CharField(max_length=500, default=None)
    reviewsAmount = models.IntegerField(default=0)
    reviewsAverage = models.FloatField(default=0)
    slug = models.SlugField(unique=True)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Publication Date")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Location, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Locations"

    def __str__(self):
        return self.name


class Spot(models.Model):
    NAME_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200

    name = models.CharField(max_length=128, unique=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    # Still need to figure this out
    # author = models.ForeignKey(
    #     settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE
    # )
    author = models.CharField(max_length = NAME_MAX_LENGTH)
    pictures = models.ImageField(upload_to="spot_images", blank=True)
    favourites = models.ManyToManyField(User, related_name='favourites',
                                        default=None, blank=True)
    postcode = models.CharField(max_length=8)
    reviewsAmount = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Publication Date")
    # url = models.URLField()
    # not going to hold reviews here just like how
    # location doesnt hold spot only other way round
    objects = models.Manager()  # default manager
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Spot, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Spots"

    def __str__(self):
        return self.name


class Review(models.Model):
    NAME_MAX_LENGTH = 128

    # 1-5 stars enums
    RATING_CHOICES = (
        (5, "5"),
        (4, "4"),
        (3, "3"),
        (2, "2"),
        (1, "1"),
    )

    title = models.CharField(max_length=NAME_MAX_LENGTH)
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE)
    # NEED TO FIGURE THIS OUT
    # author = models.ForeignKey(
    #     settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE
    # )
    author = models.CharField(max_length = NAME_MAX_LENGTH)
    comment = models.TextField(max_length=1000)
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)
    likes = models.IntegerField(default=0)
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name="Publication Date")
    comment = models.TextField(max_length=500)
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.title}: {self.rating}"

    class Meta:
        verbose_name = "Spot Review"
        verbose_name_plural = "Spot Reviews"
        ordering = ["-pub_date"]


# copied rango for user
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    pictures = models.ImageField(upload_to='profile_images', blank=True)
    # need to add favourited places
    experience = models.CharField(max_length=12)
    
    def __str__(self):
        return self.user.username


# favourites class
# class Favourite(models.Model):
#     user = models.ForeignKey('User', related_name='favourites',)
#     spot = models.ForeignKey('Spot', related_name='favourites',)

    # to get users favourite spots
    # user = User.objects.get(id='the_user_id')
    # user.favourites.values('spots')
    #
    # to get num of users who have favourited a spot
    # spot = Spot.objects.get(id='the_spot_id')
    # spot.favourites.count()
    #
    # https://stackoverflow.com/questions/64720982/modeling-favorites-in-django-from-two-different-models

    # other favourites option
    # https://github.com/sinasamavati/django-favorite/tree/master/favorite