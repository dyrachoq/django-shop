from django.contrib import admin

from .models import Category, Product

@admin.register(Category) #регистрация в админке

class CategoryAdmin(admin.ModelAdmin):
    list_display =['name', 'slug'] #это те параметры, которые будут отображатся в админке
    prepopulated_fields = {'slug': ('name',)} #будет заполнятся автоматически в соответствие с name
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'available',
                    'created', 'updated']
    list_filter = ['available', 'created', 'updated','category' ] #по каким параметрам будет фильтроваться, именно в админке
    
    list_editable = ['price', 'available']       #с помощью этого, можно быстро и спокойно менять параметры
    prepopulated_fields = {'slug': ('name',)}
# Register your models here.
