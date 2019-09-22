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


    # def save(self,commit=True):
    #     user = super(RegistrationForm,self).save(commit=False)
    #     user.first_name = self.cleaned_data['first_name']
    #     user.last_name = self.cleaned_data['last_name']
    #     user.email = self.cleaned_data['email']
    #     if commit:
    #         user.save()
    #     return user
