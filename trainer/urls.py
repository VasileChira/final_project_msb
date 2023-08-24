from django.urls import path
from trainer import views

urlpatterns = [
    path('create-trainer/', views.TrainerCreateView.as_view(), name='create-trainer'),
    path('list-of-trainer/', views.TrainerListView.as_view(), name ='list_of_trainers'),
    path('update_trainer/<int:pk>/', views.TrainerUpdateView.as_view(), name='update-trainer'),
    path('delete_trainer/<int:pk>/', views.TrainerDeleteView.as_view(), name='detele-trainer'),
    path('detail_trainer/<int:pk>/', views.TrainerDetailView.as_view(), name ='detail-trainer'),

]


