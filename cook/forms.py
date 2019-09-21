from django import forms
from .models import Food
from accounts.models import Profile,User





class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = [
        'description',
        'price',
        'quantity',
        'image'
        ]
