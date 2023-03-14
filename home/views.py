from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.db.models import Q
# Create your views here.

def home (request):
    random_cocktail = Recipe.objects.raw(f"SELECT * FROM home_recipe ORDER BY RAND() LIMIT 1")[0]
    owl_cocktail = Recipe.objects.raw(f"SELECT * FROM home_recipe ORDER BY RAND() LIMIT 8")
    random_food = Food.objects.raw(f"SELECT * FROM home_food ORDER BY RAND() LIMIT 1")[0]
    random_book = Book.objects.raw(f"SELECT * FROM home_book ORDER BY RAND() LIMIT 1")[0]
    random_articles = Article.objects.raw(f"SELECT * FROM home_article ORDER BY RAND() LIMIT 3")
    random_video = Video.objects.raw(f"SELECT * FROM home_video ORDER BY RAND() LIMIT 1")[0]
    start_index = random_video.video_url.index("v=") + 2
    url_id = random_video.video_url[start_index:start_index + 11]
    random_videos = Video.objects.raw(f"SELECT * FROM home_video WHERE NOT video_id = '{random_video.video_id}' ORDER BY RAND() LIMIT 2")
    for video in random_videos:
        start_index = video.video_url.index("v=") + 2
        url_ids = video.video_url[start_index:start_index + 11]
        video.url_id = url_ids
    context = {"random_cocktail": random_cocktail, 
               "owl_cocktail":owl_cocktail, 
               "random_food": random_food, 
               "random_book": random_book, 
               "random_articles": random_articles,
               "url_id": url_id,
               "random_videos": random_videos}
    return render(request, "home.html", context=context)

def cocktail (request, name):
    single_cocktail = Recipe.objects.get(recipe_name=name)
    alcohol = single_cocktail.recipe_alcohol.all()
    ingredients = single_cocktail.recipe_ingredients.split('&')
    steps = single_cocktail.recipe_steps.split('&')
    tools = single_cocktail.recipe_tools.all()
    suggestions = Recipe.objects.raw(f'SELECT * FROM home_recipe WHERE NOT recipe_id = "{single_cocktail.recipe_id}" ORDER BY RAND() LIMIT 4')
    context = {
                "single_cocktail": single_cocktail, 
                "alcohol": alcohol, 
                'ingredients': ingredients, 
                'steps':steps, 
                'tools':tools,
                'suggestions': suggestions}
    return render(request, "cocktail.html", context)

def cocktails (request):
    cocktails = Recipe.objects.raw(f"SELECT * FROM home_recipe")
    context = {'cocktails': cocktails}
    return render(request, "cocktails.html", context)

def food (request, name):
    single_food = Food.objects.get(food_name=name)
    trywith = single_food.food_alcohol
    ingredients = single_food.food_ingredients.split('&')
    steps = single_food.food_steps.split('&')
    suggestions = Food.objects.raw(f'SELECT * FROM home_food WHERE NOT food_id = "{single_food.food_id}" ORDER BY RAND() LIMIT 4')
    context = {
                "single_food": single_food, 
                'ingredients': ingredients, 
                'steps':steps, 
                'trywith': trywith,
                'suggestions': suggestions}
    return render(request, "food.html", context)

def foods (request):
    foods = Food.objects.raw(f"SELECT * FROM home_food")
    context = {'foods': foods}
    return render(request, "foods.html", context)

def videos (request):
    videos = Video.objects.all()
    for video in videos:
        start_index = video.video_url.index("v=") + 2
        url_id = video.video_url[start_index:start_index + 11]
        video.url_id = url_id
    context = {"videos": videos}
    return render(request, "videos.html", context)

def article (request, name):
    article = Article.objects.prefetch_related('articlesection_set').get(article_title=name)
    suggestions = Article.objects.raw(f"SELECT * FROM home_article WHERE NOT article_id = '{article.article_id}' ORDER BY RAND() LIMIT 4")
    context = {"article": article, "suggestions": suggestions}
    return render(request, "article.html", context)

def articles (request):
    articles = Article.objects.raw(f"SELECT * FROM home_article")
    context = {"articles": articles}
    return render(request, "articles.html", context)

def book(request, name):
    book = Book.objects.get(book_name = name)
    discounted_price = round(book.book_discounted_price(), 2)
    discover = book.book_description_2.split('&')
    suggested_book = Book.objects.raw(f'SELECT * FROM home_book WHERE book_id != "{book.book_id}" ORDER BY RAND() LIMIT 1')
    context = {'book': book, 'discounted_price': discounted_price, 'discover': discover, 'suggested_book': suggested_book}
    return render(request, "book.html", context)

def search(request):
    if request.method == "GET":
        searchBar = request.GET["searchBar"]
        foods = Food.objects.filter(Q(food_name__icontains=searchBar) |
                                    Q(food_type__type_name__icontains=searchBar)).distinct()
        articles = Article.objects.filter(Q(article_title__icontains=searchBar)).distinct()

        cocktails = Recipe.objects.filter(Q(recipe_name__icontains=searchBar) |
                                          Q(recipe_alcohol__alcohol_name__icontains=searchBar) |
                                          Q(recipe_tools__tool_name__icontains=searchBar)).distinct()
        context = {"cocktails": cocktails, "foods":foods, "articles":articles, "searchBar": searchBar}
        return render(request, "search.html", context)

    else:
        return render(request, "search.html")

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if Subscribe.objects.filter(subscribe_email=email).exists():
            messages.error(request, 'This email address is already subscribed.')
        else:
            subscription = Subscribe(subscribe_email=email)
            subscription.save()
            messages.success(request, 'Thank you for subscribing!')
        referer = request.META.get('HTTP_REFERER')
        if referer:
            return redirect(referer + '#subscribeInput')
    return render(request, 'index.html')