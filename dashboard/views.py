from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect



@login_required
def home_view(request):
    return render(request, 'dashboard/home.html')

@login_required   #we use this for users cannot see the dashboard page without logging in.
def dash_view(request):
    return render(request, 'dashboard/dash.html')

@login_required
def advanced_dash_view(request):
    return render(request, 'dashboard/advanced_dash.html')

@login_required
def visualization_menu(request):
    return render(request, 'dashboard/visualization_menu.html')


