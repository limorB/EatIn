
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
 path('accounts/',include('accounts.urls')),
 path('eatin/',include('feed.urls')),
 path('cart/',include('myCart.urls')),
 path('cook/',include('cook.urls')),
 path('payment/',include('payment.urls')),
 path('admin/', admin.site.urls),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
