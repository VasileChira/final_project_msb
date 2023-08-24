from django.db import models

# Create your models here.


class Trainer(models.Model):

    var_dep = (
        ('Backend', 'BACKEND'),
        ('Frontend', 'FRONTEND'),
        ('Network', 'NETWORK'),
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    course = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    departament = models.CharField(max_length=8, choices=var_dep)
    active = models.BooleanField(default=True)
    profile = models.ImageField(upload_to='profiles/', null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'




