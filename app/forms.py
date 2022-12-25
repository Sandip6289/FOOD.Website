from django import forms
from .models import ReviewTab

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewTab
        fields = ['rating', 'description']