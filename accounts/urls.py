from django.urls import path
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
    path('myorders/', views.myorders, name='myorders'),
    path('settings/', views.settings, name='settings'),
]
