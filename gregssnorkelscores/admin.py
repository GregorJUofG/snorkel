from django.contrib import admin
from gregssnorkelscores.models import Location, Spot, Review, UserProfile

class SpotAdmin(admin.ModelAdmin):
    list_display = ("name", "location")

class LocationAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class ReviewAdmin(admin.ModelAdmin):
    list_display = ("title", "spot", "comment", "rating")

admin.site.register(Spot, SpotAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(UserProfile)