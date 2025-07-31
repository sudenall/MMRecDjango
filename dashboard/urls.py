from django.urls import path
from . import views
from .views import dash_view
from django.contrib.auth import views as auth_views  #for login logout 

urlpatterns = [
    path('', views.home_view, name='home'),  # welcome, and menü
    path('charts/', views.dash_view, name='dash-view'),  # ← Dash graphs in here
    path('advanced-charts/', views.advanced_dash_view, name='advanced-dash-view'),
]
