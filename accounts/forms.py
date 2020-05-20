from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,User


class ProfileRegForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['address',"Type"]





class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    # email will now be required https://www.youtube.com/watch?v=66l9b2QrBR8
    class Meta:
        model = User
        fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'password1',
        'password2',

        ]
