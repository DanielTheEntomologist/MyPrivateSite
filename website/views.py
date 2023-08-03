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

import markdown

def test_dynamic_view(request):
    
    
    # read markdown file
    with open("website/static/md/example.md", "r") as f:
        markdown_text = f.read()

    html = markdown.markdown(markdown_text)

    context = {
        'dynamic_content': html,  # Replace with your dynamic content
    }

    return render(request, template_name="test_dynamic_view.html", context=context)
