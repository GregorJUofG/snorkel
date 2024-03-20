from django.contrib import admin
from .models import Location, Spot, Review, UserProfile

class SpotAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ("name", "url", "spotAbout")

class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class ReviewAdmin(admin.ModelAdmin):
    list_display = ("title", "spot", "comment", "rating")

admin.site.register(Spot, SpotAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(UserProfile)