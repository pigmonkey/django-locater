from django import forms

class SearchForm(forms.Form):
    RADIUS_CHOICES = (
        (10, '10 miles'),
        (25, '25 miles'),
        (50, '50 miles'),
    )
    search = forms.CharField(initial='Enter Your Location',
        widget=forms.TextInput(attrs={'class': 'location','onfocus': 'clearText(this)'}),
        help_text='You may enter a full address, a zip code, or a city and state.')
    radius = forms.ChoiceField(choices=RADIUS_CHOICES)
