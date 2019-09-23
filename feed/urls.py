from django.urls import path

from . import views

urlpatterns = [
    path('', views.display_feed, name='display_feed'),
    path('cart', views.add_to_cart, name='add_to_cart'),

]
