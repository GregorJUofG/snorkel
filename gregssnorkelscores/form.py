from django import forms
from gregssnorkelscores.models import Location, Spot, Review, User, UserProfile


class SearchForm(forms.Form):
    spot_title = forms.CharField(label = 'spot_title', max_length=80)


class LocationForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the location name.")
    favourites = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    reviewsAmount = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    reviewsAverage = forms.FloatField(widget=forms.HiddenInput(), initial=0)
    about = forms.CharField(widget=forms.HiddenInput(), required=False)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    
    class Meta:
        model = Location
        fields = ('name',)
    

class SpotForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the spot name.")
    reviewsAmount = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    postcode = forms.CharField(widget=forms.HiddenInput(), required=False)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Spot
        fields = ('name',)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title','comment',)


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'pictures',)