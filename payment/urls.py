from . import views
from django.urls import path,include


urlpatterns = [
    path('', views.display_checkout, name='display_checkout'),
    path('success/', views.make_payment, name='make_payment')

]
