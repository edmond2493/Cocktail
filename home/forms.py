from django import forms
from .models import Subscribe

class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ['subscribe_email']
