"""tanujbeta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
#from django.contrib.auth.views import views as auth_views
# from django.contrib.auth.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('paytm/', include('paytm.urls')),
    #url(r'^login/$', auth_views.login, name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('cart', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('', include('shop.urls') ),

    #path('',temp_views.redirect_to_login),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
