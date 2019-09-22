from django import forms
from .models import Food
from accounts.models import Profile,User





class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = [
        'title',
        'description',
        'category',
        'price',
        'quantity',
        'image'
        ]
