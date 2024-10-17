from django.template.response import TemplateResponse
from django.views.decorators.clickjacking import xframe_options_sameorigin

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

    context = {
        "categories": categories,
        "display_navigation_hints": display_navigation_tips,
        "page": "home",
    }

    return TemplateResponse(request, "home.html", context)


from .models import CurriculumVitae


from django.views.decorators.clickjacking import xframe_options_exempt


@xframe_options_exempt
def aboutme(request):
    categories = Category.objects.all()
    context = global_context.copy()
    context["categories"] = categories  # type: ignore
    context["page"] = "aboutme"
    cv = CurriculumVitae.objects.first()
    context["cv_file"] = cv.pdf_file.url  # type: ignore
    context["cv_name"] = cv.name  # type: ignore

    return TemplateResponse(request, "aboutme.html", context)


# import markdown

from .models import Post, Author, Category


def blog(request):
    """View blog page with all posts"""
    posts = Post.objects.all()
    categories = Category.objects.all()
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by("-timestamp")[0:3]
    context = {
        "object_list": featured,
        "latest": latest,
        "categories": categories,
        "page": "blog",
    }

    return TemplateResponse(request, "blog.html", context)


def post(request, slug):

    context = {
        "post": Post.objects.get(slug=slug),
        "categories": Category.objects.all(),
        "page": "blog",
    }

    return TemplateResponse(request, "post.html", context)


def category(request, slug):
    category = Category.objects.get(slug=slug)
    context = {
        "posts": Post.objects.filter(category=category).order_by("display_order"),
        "categories": Category.objects.all(),
        "page": "category",
    }

    return TemplateResponse(request, "category.html", context)


def categories(request):
    context = {"categories": Category.objects.all(), "page": "category"}

    return TemplateResponse(request, "categories.html", context)


def posts(request):

    context = {
        "posts": Post.objects.all(),
        "categories": Category.objects.all(),
        "page": "blog",
    }

    return TemplateResponse(request, "category.html", context)


from .models import Project


def folio(request):
    """View folio page with all projects"""

    # get all categories
    projects = Project.objects.all()
    context = {"projects": projects, "page": "folio"}

    return TemplateResponse(request, "folio.html", context)


from django.http import JsonResponse


def toggle_navigation_tips(request, slug=None):
    if request.method == "POST":
        previous_flag = request.session.get("display_navigation_tips", None)
        if previous_flag:

            request.session["display_navigation_tips"] = False
        else:

            request.session["display_navigation_tips"] = True
        return JsonResponse({"message": "Session parameter updated successfully"})
