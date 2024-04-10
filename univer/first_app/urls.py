from django.contrib import admin
from django.urls import path
from first_app import views

urlpatterns = [
    #Вызовет views.index при открытии главной страницы сайта
    path('', views.index, name="home"),
    #Вызовет views.about при /about
    path('about', views.about, name="home"),

    path('best', views.best, name="home"),

    #При использовании параметров функции-представления, параметры указываются в системе маршрутизации
    path('product/<int:id>/<str:prod_name>', views.product),
    
    #При использовании параметров строки запроса, маршрутизация не изменяется
    path('user/', views.user),
]
