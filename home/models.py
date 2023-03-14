from django.db import models

# Create your models here.

class Tool(models.Model):
    tool_id = models.AutoField(primary_key=True)
    tool_name = models.CharField(max_length=50)
    tool_image = models.ImageField(upload_to='static/media/tools')

    def __str__(self):
        return f'{self.tool_name}'

class Alcohol(models.Model):
    alcohol_id = models.AutoField(primary_key=True)
    alcohol_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.alcohol_name}'

class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.type_name}'

class Recipe(models.Model):
    recipe_id = models.AutoField(primary_key=True)
    recipe_name = models.CharField(max_length=100)
    recipe_alcohol = models.ManyToManyField(Alcohol)
    recipe_image1 = models.ImageField(upload_to='static/media/recipes')
    recipe_image2 = models.ImageField(upload_to='static/media/recipes')
    recipe_title = models.CharField(max_length=100)
    recipe_description1 = models.TextField(max_length=1000)
    recipe_description2 = models.TextField(max_length=1000, blank=True, null=True)
    recipe_ingredients = models.TextField(max_length=1000)
    recipe_steps = models.TextField(max_length=1000)
    recipe_tools = models.ManyToManyField(Tool)

    def __str__(self):
        return f'{self.recipe_name}'

class Food(models.Model):
    food_id = models.AutoField(primary_key=True)
    food_name = models.CharField(max_length=100)
    food_type = models.ManyToManyField(Type, blank=True, null=True)
    food_alcohol = models.ForeignKey(Recipe, on_delete=models.CASCADE, blank=True, null=True)
    food_image1 = models.ImageField(upload_to='static/media/food')
    food_image2 = models.ImageField(upload_to='static/media/food')
    food_title = models.CharField(max_length=100)
    food_description = models.TextField(max_length=1000)
    food_ingredients = models.TextField(max_length=1000)
    food_steps = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.food_name}'
    
class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=100)
    book_title = models.CharField(max_length=100)
    book_price = models.DecimalField(max_digits=6, decimal_places=2)
    book_discount = models.PositiveIntegerField(blank=True, null=True)
    book_image_1_1 = models.ImageField(upload_to='static/media/book')
    book_image_1_2 = models.ImageField(upload_to='static/media/book')
    book_image_1_3 = models.ImageField(upload_to='static/media/book')
    book_description_1 = models.TextField(max_length=1000)
    book_image_2_1 = models.ImageField(upload_to='static/media/book')
    book_image_2_2 = models.ImageField(upload_to='static/media/book')
    book_image_2_3 = models.ImageField(upload_to='static/media/book')
    book_description_2 = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.book_name}, {self.book_price} $'
    

    def book_discounted_price(self):
        if self.book_discount is not None:
            return self.book_price * (100 - self.book_discount) / 100
        else:
            return self.book_price
        
class Video(models.Model):
    video_id = models.AutoField(primary_key=True)
    video_url = models.CharField(max_length=255)
    video_title = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.video_title}'

class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    article_title = models.CharField(max_length=255)
    article_image = models.ImageField(upload_to='static/media/article')

    def __str__(self):
        return f'{self.article_title}'

class ArticleSection(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    section_title = models.CharField(max_length=255, blank=True, null=True)
    section_image = models.ImageField(upload_to='static/media/article', blank=True, null=True)
    section_description = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f'{self.section_title}'

class Subscribe(models.Model):
    subscribe_id = models.AutoField(primary_key=True)
    subscribe_email = models.CharField(max_length=254)
    subscribe_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.subscribe_email}'

