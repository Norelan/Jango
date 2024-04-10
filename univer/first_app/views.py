from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Вернет текст "Hello World"
def index(request):
    return HttpResponse('Hello World')

# Вернет текст "About"
def about(request):
    return HttpResponse('About')

# Вернет текст "newinfo"
def best(request):
    return HttpResponse('Передай привет маме')

########### С параметрами
#При использовании параметров функции-представления, они обрабатываются в ней, как аргументы функции
def product(request, id, prod_name):
    return HttpResponse(f"Информация о товаре: id:{id}, название:{prod_name}")

#При использовании параметров строки запроса, они получаются внутри функции-представления с помощью метода request.GET.get()
def user(request):
    #Получаем id из параметров строки запроса, по умолчанию задаем значение 10
    id = request.GET.get("id", 10)

    #Получаем user_name из параметров строки запроса, по умолчанию задаем значение Tom
    user_name = request.GET.get("user_name", "Tom")
    return HttpResponse(f"Информация о пользователе: id:{id}, имя:{user_name}")