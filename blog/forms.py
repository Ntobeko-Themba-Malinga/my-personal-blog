from django import forms
from .models import Subscriber


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder': 'Enter your email...'
                }
            )
        }


class SearchForm(forms.Form):
    query = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder': 'Search...' }))
