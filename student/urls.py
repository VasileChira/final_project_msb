from django.urls import path


from student import views

urlpatterns = [ path('create-student/', views.StudentCreateView.as_view(), name ='create_student'),
                path('list-of-students/', views.StudentListView.as_view(), name ='list_of_students'),
                path('update_student/<int:pk>/', views.StudentUpdateView.as_view(), name='update-student'),
                path('delete_student/<int:pk>/', views.StudentDeleteView.as_view(), name='detele-student'),
                path('detail_student/<int:pk>/', views.StudentDetailView.as_view(), name ='detail-student'),
                path('search/', views.search, name ="search"),

]