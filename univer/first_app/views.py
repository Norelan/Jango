from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.template.response import TemplateResponse

from django.db import models
from .forms import ProductForm, UniversityForm
from .models import Product, University


# Вернет текст "Hello World"
def index(request):
    return HttpResponse('Hello World')

# Вернет текст "About"
def about(request):
    return HttpResponse('About')

# Вернет текст "newinfo"
def best(request):
    return HttpResponse('Передай привет маме')

#При использовании параметров строки запроса, они получаются внутри функции-представления с помощью метода request.GET.get()
def user(request):
    #Получаем id из параметров строки запроса, по умолчанию задаем значение 10
    id = request.GET.get("id", 10)

    #Получаем user_name из параметров строки запроса, по умолчанию задаем значение Tom
    user_name = request.GET.get("user_name", "Tom")
    data = {"user_name" : user_name, "user_id" : id}
    return TemplateResponse(request, "user.html", data)
    # return HttpResponse(f"Информация о пользователе: id:{id}, имя:{user_name}")

def numbers(request):
    number = int(request.GET.get("n", 0))
    nums_info = []
    for n in range(number):
        if n % 2 == 0:
            nums_info.append((n, 0))
        else:
            nums_info.append((n, 1))
    data = {"nums_info": nums_info}
    return TemplateResponse(request, "numbers.html", data)

########### С параметрами

#При использовании параметров функции-представления, они обрабатываются в ней, как аргументы функции
def product(request, prod_id):
    try:
        curr_prod = Product.objects.get(id=prod_id)
        data = {"prod_name": curr_prod.name, "prod_birth":curr_prod.birth, "prod_uni":curr_prod.univer, "prod_year":curr_prod.year}
        return TemplateResponse(request, "product.html", data)
    except Product.DoesNotExist:
        return HttpResponseNotFound("Продукта с таким id не существует")

def create_product(request):
    if request.method == "POST":
        #Если мы ввели данные в формы, и нажали на кнопку "Send Product", то тогда метод запроса будет POST(как мы указали в шаблоне),
        #и соответственно, выполнится этот блок, который просто перенаправит нас на страницу с информацией об продукте
        #form = ProductForm(request.POST)
        prod_name = request.POST.get("name")
        prod_birth = request.POST.get("birth")
        prod_univer_id = request.POST.get("univer")
        prod_univer = University.objects.get(id=prod_univer_id )
        prod_year = request.POST.get("year")

        #prod_univer = form.cleaned_data["univer"]
         #Добавляем продукт в базу данных
        product = Product.objects.create(name = prod_name, birth = prod_birth, univer = prod_univer, year = prod_year)
        #Получаем id добавленного для того, чтобы перейти на его страницу
        new_id = product.id
        return HttpResponseRedirect(f"/first_app/product/{new_id}")
    else:
        #Если же мы просто открыли страницу, то выполнится этот блок, который выведет нам форму
        data = {"form": ProductForm()}
        return TemplateResponse(request, "create_prod.html", data)
    
def delete_product(request, prod_id):
    try:
        product = Product.objects.get(id=prod_id)
        product.delete()
        return HttpResponseRedirect("/first_app/product/")
    except Product.DoesNotExist:
        return HttpResponseNotFound("Продукта с таким id не существует")

def product_list(request):
    #Получаем все продукты из базы
    all_prods = Product.objects.all()
    data = {"products": all_prods}
    return TemplateResponse(request, "product_list.html", data)


def university(request, uni_id):
    try:
        curr_uni = University.objects.get(id=uni_id)
        data = {"uni_name": curr_uni.name, "uni_short_name":curr_uni.short_name, "uni_year":curr_uni.year}
        return TemplateResponse(request, "university.html", data)
    except University.DoesNotExist:
        return HttpResponseNotFound("Университета с таким id не существует")
    
def create_university(request):
    if request.method == "POST":
        #Если мы ввели данные в формы, и нажали на кнопку "Send Product", то тогда метод запроса будет POST(как мы указали в шаблоне),
        #и соответственно, выполнится этот блок, который просто перенаправит нас на страницу с информацией об продукте
        #form = ProductForm(request.POST)
        prod_name = request.POST.get("name")
        prod_short_name = request.POST.get("short_name")
        prod_year = request.POST.get("year")

        #prod_univer = form.cleaned_data["univer"]
         #Добавляем продукт в базу данных
        university = University.objects.create(name = prod_name, short_name = prod_short_name, year = prod_year)
        #Получаем id добавленного для того, чтобы перейти на его страницу
        new_id = university.id
        return HttpResponseRedirect(f"/first_app/university/{new_id}")
    else:
        #Если же мы просто открыли страницу, то выполнится этот блок, который выведет нам форму
        data = {"form": UniversityForm()}
        return TemplateResponse(request, "create_university.html", data)
    
def university_list(request):
    #Получаем все продукты из базы
    all_prods = University.objects.all()
    data = {"universities": all_prods}
    return TemplateResponse(request, "university_list.html", data)

def delete_university(request,uni_id):
    try:
        univer = University.objects.get(id=uni_id)
        univer.delete()
        return HttpResponseRedirect("/first_app/university/")
    except University.DoesNotExist:
        return HttpResponseNotFound("Университета с таким id не существует")