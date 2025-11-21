from django.contrib import admin
from django.urls import path, include
from playground import views
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('playground/', include('playground.urls')),
    path('api/', include('storefront.api_urls')),
    
    
]