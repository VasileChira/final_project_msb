from django.contrib.auth.models import User
from django.db import models
# from django.db.models import CASCADE

# Create your models here.

class Product(models.Model):

    name = models.CharField(max_length=200)
    price = models.IntegerField()

#auto_now_add=  stocheaza data si ora cand a fost adaugata inregistrarea. Nu se mai mdofiica
#auto_now = cand a fost adaugata inreg. aceasta se modifica daca se realizeaza modificari pe inregistrare
    def __str__(self):
        return  f'{self.name} {self.price}'