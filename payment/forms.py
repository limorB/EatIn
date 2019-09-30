from django import forms
from .models import Order
from accounts.models import Profile



class PaymentForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['payment_method']
