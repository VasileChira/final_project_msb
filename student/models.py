from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE

import userextend
from trainer.models import Trainer


# Create your models here.

class Student(models.Model):

    gender_options = (
        ('Male','MALE'),
        ('female', 'FEMALE')
    )

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.EmailField(max_length=100)
    description = models.TextField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default= True)
    gender = models.CharField(max_length=6, choices=gender_options)
    trainer = models.ForeignKey(Trainer, on_delete=CASCADE, null=True)
    profile = models.ImageField(upload_to='profile_student/', null=True)

    created_at = models.DateTimeField(auto_now_add= True)
    update_at = models.DateTimeField(auto_now=True)


#auto_now_add=  stocheaza data si ora cand a fost adaugata inregistrarea. Nu se mai mdofiica
#auto_now = cand a fost adaugata inreg. aceasta se modifica daca se realizeaza modificari pe inregistrare
    def __str__(self):
        return  f'{self.first_name} {self.last_name}'


class HistoryStudent(models.Model):
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=CASCADE, null=True)

    def __str__(self):
        return self.message

