from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.conf import settings
from django.urls import reverse

# from catalog.models import Spots  copied from website idk yet what our equivalent of catalog is

###############
# REVIEWS
# https://michaelstromer.nyc/books/intro-to-django/django-reviews
#################


class Location(models.Model):
    NAME_MAX_LENGTH = 128

    name = models.CharField(max_length=128, unique=True) # (We will want location names to be unique)
    pictures = models.ImageField(upload_to="location_images", blank=True)
    about = models.CharField(max_length=500, default="Default text :)")
    reviewsAmount = models.IntegerField(default=0)
    reviewsAverage = models.FloatField(default=0)
    slug = models.SlugField(null=False, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Location, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Locations"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'location_name_slug': self.slug})


class Spot(models.Model):

    class NewManager(models.Manager):
        def get_queryset(self) -> models.QuerySet:
            return super().get_queryset()

    NAME_MAX_LENGTH = 128
    URL_MAX_LENGTH = 200

    def get_default_location():
        return Location.objects.get_or_create(name="Default")[0]

    name = models.CharField(max_length=128, unique=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=get_default_location, )
    # Still need to figure this out
    # author = models.ForeignKey(
    #     settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE
    # )
    author = models.CharField(max_length = NAME_MAX_LENGTH)
    pictures = models.ImageField(upload_to="spot_images", blank=True)
    reviewsAmount = models.IntegerField(default=0)
    slug = models.SlugField(null=False, unique=True)
    favourites = models.ManyToManyField(User, related_name='favourites', default=None, blank=True)
    objects = models.Manager()  # default manager
    newmanager = NewManager() # custom manager

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Spot, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Spots"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('service_detail', kwargs={'spot_name_slug': self.slug})


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

    #default spot
    def get_default_spot():
        return Spot.objects.get_or_create(name='Default')[0]

    title = models.CharField(max_length=NAME_MAX_LENGTH)
    spot = models.ForeignKey(Spot, on_delete=models.CASCADE, default=get_default_spot, )
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE
    )
    comment = models.TextField(max_length=1000)
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)
    likes = models.IntegerField(default=0)
    comment = models.TextField(max_length=500)
    rating = models.IntegerField(choices=RATING_CHOICES, default=1)
    likes = models.IntegerField(default=0)

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title}: {self.rating}"

    class Meta:
        verbose_name = "Spot Review"
        verbose_name_plural = "Spot Reviews"


# copied rango for user
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Define choices for experience level
    EXPERIENCE_LEVELS = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Expert', 'Expert'),
    )

    website = models.URLField(blank=True)
    pictures = models.ImageField(upload_to='profile_images', blank=True)
    experience = models.CharField(max_length=12, choices=EXPERIENCE_LEVELS, default='Beginner')

    def __str__(self):
        return self.user.username
