from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cocktail/<name>', views.cocktail, name='cocktail'),
    path('cocktails', views.cocktails, name='cocktails'),
    path('food/<name>', views.food, name='food'),
    path('foods', views.foods, name='foods'),
    path('article/<name>', views.article, name='article'),
    path('articles', views.articles, name='articles'),
    path('videos', views.videos, name='videos'),
    path('search', views.search, name='search'),
    path('book/<name>', views.book, name='book'),
    path('subscribe/', views.subscribe, name='subscribe'),
]