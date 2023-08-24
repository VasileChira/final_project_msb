from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import ProductForm
from .models import Product


# Create your views here.
@login_required()
def hello(request):
    return HttpResponse('Hello World!')


@login_required()
def name(request):
    return HttpResponse('Stefania')


@login_required()
def cars(request):
    list_cars = {
        'all_cars': [
            {
                'brand': 'VW',
                'model': 'Golf6',
                'year': 2020
            },
            {
                'brand': 'BMW',
                'model': 530,
                'year': 2021
            },
            {
                'brand': 'audi',
                'model': 'a6',
                'year': 2023
            }
        ]
    }

    return render(request, 'intro/list_of_cars.html', list_cars)


# def products(request):
#     list_products = {
#         "listproducts": [
#             {
#                 "id": 1,
#                 "Nume": 'Canapea',
#                 "Magazin": 'Altex',
#                 "Pret": 3000,
#             },
#             {
#                 "id": 2,
#                 "Nume": 'Masa',
#                 "Magazin": 'Domo',
#                 "Pret": 1200,
#
#             },
#             {
#                 "id": 3,
#                 "Nume": 'Scaun',
#                 "Magazin": 'Flanco',
#                 "Pret": 400,
#             }
#         ]
#     }
#     return render(request, 'intro/list_of_products.html', list_products)
@login_required()
def products(request):
    products = Product.objects.all()
    context = {
        'listproducts': products
    }
    return render(request, 'intro/list_of_products.html', context)



class UpdatePrice(LoginRequiredMixin,UpdateView):
    model= Product
    form_class = ProductForm
    template_name = 'intro/update_template.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('list-of-products')

# def updateprice(request,id):
#     product = get_object_or_404(Product, pk = id)
#     if request.method == 'POST':
#         form = ProductForm(request.POST, instance= product)
#         if form.is_valid():
#             form.save()
#             return redirect('list-of-products')
#
#     form = ProductForm(instance=product)
#     context ={
#         'form': form,
#         'product': product
#      }
#     return render(request,'intro/update_template.html', context)


class DeleteProduct(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'intro/delete_template.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('list-of-products')
