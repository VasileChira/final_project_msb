from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

import student
import userextend
from student.forms import StudentForm, StudentUpdateForm
from student.models import Student, HistoryStudent


# Create your views here.

#createview = folost pt a genera un formular pe baza modelului si pt a salba datele in bd
#succesmessagemixin - folosit pt a afisa un mesaj de succes in momentul in care actiunea a fost realizata cu succes
# PermissionReuiredMixin -> verificam daca userul logat are permisiunea respectiva, daca user logat NU ARE permisiunea
# respectiva va fi redirectionat catre pagina 403 (HTTP STATUS)

class StudentCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'student/create_student.html'
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('list_of_students')
    success_message ="{f_name} {l_name}"
    permission_required = 'student.add_student'

    #get succes message e o metoda specifica clasei succes
    def get_success_message(self, cleaned_data):
        if self.object.gender == 'male':
            message = self.success_message + ' ' + 'a fost adaugat cu succes'
        else:
            message = self.success_message + ' ' + 'a fost adaugata cu succes'

        return message.format(f_name=self.object.first_name, l_name=self.object.last_name)

    def form_valid(self, form):
        if form.is_valid():
            newstud = form.save(commit=False)
            get_current_user = self.request.user.id
            username_user = User.objects.get(id = get_current_user)
            get_message = f' Studentul {newstud.first_name} a fost adaugat cu succes de catre {username_user}'

            HistoryStudent.objects.create(message=get_message, created_at=datetime.now(), active=True, user_id=self.request.user.id)


        return redirect('create_student')




#Listview - folosim pt a afisa inregistrarile din tabela

class StudentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = 'student/list_of_students.html'
    model = Student
    context_object_name = 'allstudents' #denumirea pt a prelua datele si face query =Student.object.all()
    permission_required = 'student.view_list_of_students'

    # metoda get_queryset este o metoda utlizata in clasele bazate pe vizualizare in Django pentru a obtine
    # si returna setul de obiecte (QuerySet) care va fi folosit pentru a afisare.
    def get_queryset(self):
        return Student.objects.filter(active=True)


#updateview- pt a actualiza date in bd


class StudentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Student
    template_name ='student/update_student.html'
    form_class = StudentUpdateForm
    success_url = reverse_lazy('list_of_students')
    permission_required = 'student.change_students'

class StudentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Student
    template_name = 'student/delete_student.html'
    # pk_url_kwarg = 'id'
    success_url = reverse_lazy('list_of_students')
    permission_required = 'student.delete_student'


class StudentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Student
    template_name = 'student/details_student.html'
    permission_required = 'student.view_student'


#icontains- atribut care cauta string in string
@login_required()
def search(request):
    get_value = request.GET.get('filter')
    if get_value:
        students = Student.objects.filter(Q(last_name__icontains =get_value) | Q(first_name__icontains = get_value))
    else:
        students = Student.objects.all()
    return render(request, 'student/list_of_students.html',{'allstudents': students})