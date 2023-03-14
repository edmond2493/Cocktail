from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Recipe)
admin.site.register(Food)
admin.site.register(Tool)
admin.site.register(Alcohol)
admin.site.register(Type)
admin.site.register(Book)
admin.site.register(Video)
admin.site.register(Subscribe)

class ArticleSectionInline(admin.TabularInline):
    model = ArticleSection
    extra = 1

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleSectionInline]