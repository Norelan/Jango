from django.contrib import admin
from .models import Product, University

# Register your models here.
#Создаем специальный класс, в котором можно указывать различные параметры работы с моделью через панель администратора
class ProductAdmin(admin.ModelAdmin):
    #Данная переменная указывает на поля, которые будут выводится в списке продуктов
    list_display = ('id', 'name', 'cost')

admin.site.register(Product, ProductAdmin)

class UniversityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
admin.site.register(University, UniversityAdmin)