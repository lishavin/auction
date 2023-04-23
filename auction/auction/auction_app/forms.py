from django import forms
from .models import item

class itemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = ['phone', 'image', 'name', 'info', 'min_bid']