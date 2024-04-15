from django.db import models

# Create your models here.

class University(models.Model):
    name = models.CharField(verbose_name = "Название", max_length=100)
    short_name = models.CharField(verbose_name = "Сокращенное название", max_length=10)
    year =  models.CharField(verbose_name = "Дата создания", max_length=10)

        #Переопределение метода str() нужно для того, чтобы вместо Company object(id) писалось просто название компании
    def __str__(self):
        return self.name
    
class Product(models.Model):
    
    name = models.CharField(verbose_name = "ФИО", max_length=50)
    birth = models.CharField(verbose_name = "Дата рождения", max_length=10)
    #null = True указывает на то, что поле может иметь значение null
    #on_delete указывает на то, что необходимо делать в случае удаления производителя из базы. В данном случае мы устанавливаем поле в null
    univer = models.ForeignKey(University, on_delete = models.SET_NULL, null=True,verbose_name = "Университет")
    year = models.IntegerField(verbose_name = "Год поступления")
    def __str__(self):
        #return f"{self.name}_{self.cost}"
        return self.name