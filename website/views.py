from django.shortcuts import render

# Create your views here.

def index(request):
    """View index page for now only with Daniel's page"""
    display_navigation_tips = request.session.get('display_navigation_tips',"displaynavigationtips defaulted")

    # get all categories
    categories = Category.objects.all()
    
    
    context = {
        'categories': categories
        ,"display_navigation_hints":display_navigation_tips
    }
    
    return render(request, template_name="index.html", context=context)

def aboutme(request):
    categories = Category.objects.all()
    context = {}
    context["categories"] = categories
    return render(request, template_name="aboutme.html",context=context)

import markdown

from .models import Post, Author, Category

def blog(request):
    """View blog page with all posts"""
    posts = Post.objects.all()
    categories = Category.objects.all()
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    context= {
        'object_list': featured,
        'latest': latest,
        'categories':categories,
    }
    return render(request, 'blog.html', context)
    
def post(request,slug):
    post = Post.objects.get(slug=slug)
    categories = Category.objects.all()
    context = {
        'post': post,
    }
    context["categories"] = categories
    return render(request, 'post.html', context)

def category(request,slug):
    category = Category.objects.get(slug=slug)
    categories = Category.objects.all()
    posts_in_category = Post.objects.filter(category=category).order_by("display_order")
    
    context = {
        'posts': posts_in_category,
    }
    context["categories"] = categories
    return render(request, 'category.html', context)

def categories(request):
    #get all categories
    categories = Category.objects.all()
    
    context = {
        'categories': categories,
    }
    return render(request, 'categories.html', context)

from django.http import JsonResponse

def toggle_navigation_tips(request,slug=None):
    if request.method == 'POST':
        previous_flag = request.session.get("display_navigation_tips",None)
        if previous_flag:
            
            request.session['display_navigation_tips'] = False
        else:
            
            request.session['display_navigation_tips'] = True
        return JsonResponse({'message': 'Session parameter updated successfully'})
    
    # return render(request, 'toggle_navigation_tips.html')
    
    

