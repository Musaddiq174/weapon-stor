from django.contrib import admin
from .models import Shop, Product
from .models import Choice, Question
class ChoiceInline(admin.TabularInline): ...

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    #list_display = ["question_text", "pub_date"]
    list_display = ["question_text", "pub_date", "was_published_recently"]



admin.site.register(Question, QuestionAdmin)





# admin.py


class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'description')
    search_fields = ('name', 'location')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'shop', 'price', 'pub_date', 'expire_date')  # Keep is_expired here
    search_fields = ('name', 'shop__name')
    list_filter = ('shop', 'pub_date', 'expire_date')



# Register your models
admin.site.register(Shop, ShopAdmin)
admin.site.register(Product, ProductAdmin)

