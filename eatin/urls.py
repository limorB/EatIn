
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
 path('accounts/',include('accounts.urls')),
 path('feed/',include('feed.urls')),
 path('cart/',include('myCart.urls')),
 path('cook/',include('cook.urls')),
 path('payment/',include('payment.urls')),
 path('admin/', admin.site.urls),
]
