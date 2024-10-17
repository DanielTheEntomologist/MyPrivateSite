# website.urls

from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from website import views

urlpatterns = [
    path("", views.folio, name="folio"),
    path("home", views.home, name="home"),
    path("aboutme", views.aboutme, name="aboutme"),
    path("post", views.posts, name="post"),
    path("post/", views.posts, name="post"),
    path("post/<slug>/", views.post, name="post"),
    path("category", views.categories, name="category"),
    path("category/", views.categories, name="categories"),
    path("category/<slug>/", views.category, name="category"),
]

from django.urls import re_path
from django.views.static import serve

urlpatterns += [
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT})
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
