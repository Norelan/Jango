from django.db import models

# Create your models here.

class University(models.Model):
    name = models.CharField(verbose_name = "Название", max_length=20)

        #Переопределение метода str() нужно для того, чтобы вместо Company object(id) писалось просто название компании
    def __str__(self):
        return self.name
    
class Product(models.Model):
    cost = models.IntegerField(verbose_name = "Цена")
    name = models.CharField(verbose_name = "Название", max_length=20)
    #null = True указывает на то, что поле может иметь значение null
    #on_delete указывает на то, что необходимо делать в случае удаления производителя из базы. В данном случае мы устанавливаем поле в null
    univer = models.ForeignKey(University, on_delete = models.SET_NULL, null=True,verbose_name = "университет")

    def __str__(self):
        return f"{self.name}_{self.cost}"