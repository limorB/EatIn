from django.shortcuts import render
from django.http import HttpResponse


def display_checkout(request):
    return render(request, 'payment/index.html')
