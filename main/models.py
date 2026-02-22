from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)  #db_index=True позволяет при фильтрации искать категории именно по name
    slug = models.SlugField(max_length=100, unique=True) #это грубо говоря человечиский url, который меняет с /product/55 на /product/plush-toy
    
    class Meta:
        ordering = ('name',) # сортировка по умолчанию, в данном случае сортировка по name
        verbose_name = 'Категория' #перевод с англ на русс
        verbose_name_plural = 'Категорий' #перевод множественного на русс
        
    def __str__(self):   #отображение в админке категорий по имени, будет не <Category object (1)>, а нормальное название
        return self.name
    
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', #ForeignKey - связь, продукт ссылается на категорию; related_name='products' - даем имя, на которое будем ссылаться.
                                 on_delete=models.CASCADE) #on_delete=models.CASCADE - если у нас там есть категория с товарами, и если мы ее захотим удалить, то выскочит плашка предупреждением, что будет удалены все созданные продукты под этой категорией
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True) #blank=true, поле image может быть пустым
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2) #лучше для высчитывания скидок и т.д. лучше чем IntegerField; decimal_places=2, срез, то есть будет не 10.345345345, а будет 10.35
    available = models.BooleanField(default=True) #default true, то есть товар доступен, уже будет отмечен флажок, bool - true или false
    created = models.DateTimeField(auto_now_add=True) #то есть дата создания будет автоматически добавляться
    updated = models.DateField(auto_now=True) #автоматически обновится последняя дата изменения товара
    
    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name
    