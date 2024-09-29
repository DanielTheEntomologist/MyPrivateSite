from django.shortcuts import render

global_context = {
    "name": "Daniel",
    "surname": "Borowiecki",
    "title": "Daniel's Blog",
    "author": "Daniel",
    "description": "This is a blog about Python and Django",
    "keywords": "Python, Django, Web Development",
}

# Create your views here.

def home(request):
    """View home page"""
    # display_navigation_tips = request.session.get('display_navigation_tips',"displaynavigationtips defaulted")
    display_navigation_tips = False

    # get all categories
    categories = Category.objects.all()

    local_context = {
        'categories': categories
        ,"display_navigation_hints":display_navigation_tips
    }
    context = {**global_context, **local_context}
    
    return render(request, "home.html", context)

def aboutme(request):
    categories = Category.objects.all()
    context = global_context.copy()
    context["categories"] = categories
    return render(request, template_name="aboutme.html",context=context)

# import markdown

from .models import Post, Author, Category

def blog(request):
    """View blog page with all posts"""
    posts = Post.objects.all()
    categories = Category.objects.all()
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    local_context= {
        'object_list': featured,
        'latest': latest,
        'categories':categories,
    }
    context = {**global_context, **local_context}
    return render(request, 'blog.html', context)
    
def post(request,slug):
    
    local_context = {
        'post': Post.objects.get(slug=slug),
        'categories': Category.objects.all(),
    }
    context = {**global_context, **local_context}
    return render(request, 'post.html', context)

def category(request,slug):
    category = Category.objects.get(slug=slug)
    local_context = {
        'posts': Post.objects.filter(category=category).order_by("display_order"),
        "categories": Category.objects.all()
    }
    context = {**global_context, **local_context}
    return render(request, 'category.html', context)

def categories(request):
    local_context = {
        'categories': Category.objects.all(),
    }
    context = {**global_context, **local_context}
    return render(request, 'categories.html', context)

def posts(request):
    
    local_context = {
        'posts': Post.objects.all(),
        'categories': Category.objects.all(),
    }
    context = {**global_context, **local_context}
    return render(request, 'category.html', context)

from django.http import JsonResponse

def toggle_navigation_tips(request,slug=None):
    if request.method == 'POST':
        previous_flag = request.session.get("display_navigation_tips",None)
        if previous_flag:
            
            request.session['display_navigation_tips'] = False
        else:
            
            request.session['display_navigation_tips'] = True
        return JsonResponse({'message': 'Session parameter updated successfully'})

    
    

