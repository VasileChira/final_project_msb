from django.urls import path

from intro import views

urlpatterns = [
    path('first_page/', views.hello, name='first-page'),
    path('show_name/', views.name, name='show-name'),
    path('list_of_cars/', views.cars, name='list-of-cars'),
    path('list_of_products/', views.products, name = 'list-of-products'),
    path('update/<int:id>/', views.UpdatePrice.as_view(), name ='change-price'),
    path('delete/<int:id>/', views.DeleteProduct.as_view(), name ='delete-product')
]


# PREFIXUL ESTE UNIC
# NAME ESTE UNIC
# FIEACARE PATH VA AVEA O FUNCTIE/CLASA.

