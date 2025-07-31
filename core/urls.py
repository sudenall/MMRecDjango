"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lambda request: redirect('dashboard/')),
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),  
    path('django_plotly_dash/', include('django_plotly_dash.urls')), 
    path('accounts/', include('django.contrib.auth.urls')), # django's ready auth system , In this way, ready-made views such as /accounts/login/, /accounts/logout/, /accounts/password_change/ work automatically with the help of Django's ready-made login/logout system
    path("accounts/", include("accounts.urls")), #for custom user registreation
    path('customdash/', include('customdash.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#/accounts/register/ → Senin kendi formunla kullanıcı kaydeder

#/accounts/login/ → Django’nun hazır login sayfası

#/accounts/logout/ → Logout işlemi gerçekleşir