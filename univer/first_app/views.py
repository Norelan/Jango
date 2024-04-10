from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template.response import TemplateResponse


from .forms import ProductForm

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
def product(request, cost, prod_name):
    return HttpResponse(f"Цена товара :{cost}, название:{prod_name}")

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

def create_product(request):
    if request.method == "POST":
        #Если мы ввели данные в формы, и нажали на кнопку "Send Product", то тогда метод запроса будет POST(как мы указали в шаблоне),
        #и соответственно, выполнится этот блок, который просто перенаправит нас на страницу с информацией об продукте
        prod_name = request.POST.get("name")
        prod_cost = request.POST.get("cost")
        return HttpResponseRedirect(f"/first_app/product/{prod_cost}/{prod_name}")
    else:
        #Если же мы просто открыли страницу, то выполнится этот блок, который выведет нам форму
        data = {"form": ProductForm()}
        return TemplateResponse(request, "create_prod.html", data)