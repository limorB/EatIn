from . import views
from django.urls import path,include


urlpatterns = [
    path('', views.display_checkout, name='display_checkout'),
    path('paypal/', include('paypal.standard.ipn.urls')),
]
