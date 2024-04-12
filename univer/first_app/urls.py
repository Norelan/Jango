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
    path('product/<int:prod_id>/', views.product),
    
    #При использовании параметров строки запроса, маршрутизация не изменяется
    path('user/', views.user),

    #
    path('nums/', views.numbers),

    path('product/create/', views.create_product),

    path('product/', views.product_list),

    path('product/delete/<int:prod_id>/', views.delete_product),
]
