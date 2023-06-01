from django.shortcuts import render

# Create your views here.

# todo - programatically create views 

def welcome(request):
    """View landing page with choice of people"""
    return render(request, template_name="welcome.html")

def index(request):
    """View index page for now only with Daniel's page"""
    return render(request, template_name="tower.html")

def experiments(request):
    return render(request, template_name="experiments.html")

def aboutme(request):
    return render(request, template_name="aboutme.html")

def tower(request):
    return render(request, template_name="tower.html")

def tower_explanation(request):
    return render(request, template_name="tower_explanation.html")

def heroku_explanation(request):
    return render(request, template_name="heroku_explanation.html")

def advent_explanation(request):
    return render(request, template_name="advent_explanation.html")

from django.shortcuts import redirect

def redirect_daniel(request):
    response = redirect('welcome')
    return response