
from django.urls import path
from .views import(
    HomeView,
)

app_name ='carousel'

urlpatterns = [
    # Home
    path('', HomeView, name='home'),

]