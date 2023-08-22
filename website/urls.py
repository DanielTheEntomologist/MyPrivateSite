#website.urls

from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from website import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('welcome', views.welcome, name='welcome'),
    path('index', views.index, name='index'),
    path('tower', views.tower, name='tower'),
    path('experiments', views.experiments, name='experiments'),
    path('aboutme', views.aboutme, name='aboutme'),
    path('tower_explanation', views.tower_explanation, name='tower_explanation'),
    path('heroku_explanation', views.heroku_explanation, name='heroku_explanation'),
    path('advent_explanation', views.advent_explanation, name='advent_explanation'),
    path('test_dynamic_view', views.test_dynamic_view, name='test_dynamic_view'),
    
    path('post', views.post, name='post'),
    path('post/<slug>/', views.post, name = 'post'),
    path('category', views.categories, name='categories'),
    path('category/<slug>/', views.category, name = 'category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT )
    