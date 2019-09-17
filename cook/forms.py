from django import forms
from .models import Food
from accounts.models import Food




class FoodForm(forms.ModelForm):
    class Meta:
        model = Food
        exclude = ["user"]
