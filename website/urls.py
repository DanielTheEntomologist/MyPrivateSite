#website.urls

from django.urls import path, include
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
    path('advent_explanation', views.advent_explanation, name='advent_explanation')
]