from django import forms
from gregssnorkelscores.models import Location, Spot, Review, User, UserProfile


class SearchForm(forms.Form):
    spot_title = forms.CharField(label = 'spot_title', max_length=80)


class LocationForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the location name")
    reviewsAmount = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    reviewsAverage = forms.FloatField(widget=forms.HiddenInput(), initial=0)
    about = forms.CharField(max_length=1000, help_text="About location")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Location
        fields = ('name',)
    

class SpotForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the spot name.")
    spotAbout = forms.CharField(max_length=200, 
                            help_text="Please enter a bit about your spot")
    pictures = forms.ImageField(help_text="Enter a picture here", required=False)
    reviewsAmount = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Spot
        fields = ('name',)

class ReviewForm(forms.ModelForm):
    title = forms.CharField(max_length=25,
                            help_text="Please enter the title of your review")
    comment = forms.CharField(max_length=500,
                              help_text="Please enter the contents of your review")
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    rating = forms.IntegerField(max_value=5, min_value=1, required=True,
                                help_text="Please rate this spot here")
    class Meta:
        model = Review
        fields = ('title','comment','rating')
        widgets = {
            'rating': forms.RadioSelect()  # Ensures the rating field uses radio buttons
        }


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'pictures',)