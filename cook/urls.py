from . import views
from django.urls import path


urlpatterns = [
    path('', views.food_upload, name='food_upload'),
]
