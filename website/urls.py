#website.urls

from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from website import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('aboutme', views.aboutme, name='aboutme'),
    path('post', views.post, name='post'),
    path('post/<slug>/', views.post, name = 'post'),
    path('category', views.categories, name='categories'),
    path('category/<slug>/', views.category, name = 'category'),
    path('toggle-navigation-tips', views.toggle_navigation_tips, name='toggle_navigation_tips'),
    path('category/<slug>/toggle-navigation-tips', views.toggle_navigation_tips, name='toggle_navigation_tips'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT )
    