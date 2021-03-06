from . import views
from django.urls import path


urlpatterns = [
    path('', views.display_cart, name='display_cart'),
    # path('', views.remove_from_cart, name='remove_from_cart'),
    # path('remove', views.remove_from_cart, name='remove_from_cart'),
    path('remove/<int:id>', views.remove_from_cart, name='remove_from_cart'),
    path('update/<int:id>', views.update_quantity, name='update_quantity')

]
