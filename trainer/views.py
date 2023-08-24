from datetime import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from student.models import Student
from trainer.forms import TrainerForm, TrainerUpdateForm
from trainer.models import Trainer


class TrainerCreateView(LoginRequiredMixin, CreateView):
    template_name = 'trainer/create_trainer.html'
    model = Trainer
    form_class = TrainerForm
    success_url = reverse_lazy('home-page')


class TrainerListView(LoginRequiredMixin, ListView):
    template_name = 'trainer/list_of_trainers.html'
    model = Trainer
    context_object_name = 'alltrainers'
    #
    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['trainers'] = Trainer.objects.all()
    #     trainer_students =


class TrainerUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Trainer
    template_name = 'trainer/update_trainer.html'
    form_class = TrainerUpdateForm
    success_url = reverse_lazy('list_of_trainers')
    success_message = 'Trainer-ul {f_name} {l_name} a fost actualizat cu succes!'

    def get_success_message(self, cleaned_data):
        return self.success_message.format(f_name=self.object.first_name, l_name=self.object.last_name)


class TrainerDeleteView(LoginRequiredMixin, DeleteView):
    model = Trainer
    template_name = 'trainer/delete_trainer.html'
    # pk_url_kwarg = 'id'
    success_url = reverse_lazy('list_of_trainers')


class TrainerDetailView(LoginRequiredMixin, DetailView):
    model = Trainer
    template_name = 'trainer/details_trainer.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = datetime.now()
        #creez o cheie noua a dictionarului la care adaug ca valoare
        context['current_date'] = now

        current_trainer_id = self.kwargs['pk'] # avem acces la id ul trainerului respectiv

        students_trainer = Student.objects.filter(trainer_id= current_trainer_id) #iau toti sudentii aignati trainerului
        context['students'] = students_trainer #trimit in interfata toti studentii asignati trainerului curent

        return context



# get_context_data este o metoda folosita in clasele DetailView, Listview, TemplateView, Updateview etc
# care este utilizata pt a construi si returna un dictionar de date de context care vor fi afisate in paginile html
