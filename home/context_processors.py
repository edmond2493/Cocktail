from .models import *

def navCategory(request):
    unique_alcohols = Recipe.objects.order_by('?').values_list('recipe_alcohol__alcohol_name', flat=True).distinct()[:6]
    unique_food = Food.objects.order_by('?').values_list('food_type__type_name', flat=True).distinct()[:4]
    context = {"unique_alcohols": unique_alcohols, "unique_food": unique_food}
    return (context)