from django.shortcuts import render, get_object_or_404

from .models import Category, Product




def product_list(request, category_slug=None): #request - клиент, всегда пишется
    categories = Category.objects.all() #берем все категории из бд
    products = Product.objects.filter(available = True)
    
    category = None 
    
    if category_slug:
        category = get_object_or_404(Category, category_slug=category_slug)
        products = products.filter(category=category)
        
    return render(request, 'main/product/list.html', #в какой файл заносим данные
                  {'category': category,  #что кладем в файл html
                   'categories': categories,
                   'products': products})

