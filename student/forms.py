from django import forms

from django.forms import TextInput, NumberInput, EmailInput, Textarea, DateInput, Select

from student.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age','email','description',
                  'start_date', 'end_date', 'active','gender','trainer','profile']  #specific ce fields vreau in forms si ordinea lor

#widgets personalizez camp din formular, ce tip de data accepta, cum sa arate si sa se comporte
        #in attrs trec atribute html
        widgets ={
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your last name'}),
            'age': NumberInput(attrs={'class': 'form-control',"placeholder":"Enter your age"}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your email'}),
            'description': Textarea(attrs={"class":"form-control",'placeholder': 'Enter Your description', 'rows':3}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),  # type -> datetime-local
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),  # type -> datetime-local
            'gender': Select(attrs={'class': 'form-select'}),
            'trainer': Select(attrs={'class':'form-select'})
        }


    def clean(self):
        cleaned_date = self.cleaned_data  #se genereaza un dictionar cu datele completate din formular
        print(cleaned_date)

        #unicitate pe adresa de email
        get_email = cleaned_date.get('email')
        check_email = Student.objects.filter(email = get_email)
        if check_email:
            msg = 'Exista deja aceasta adresa de email'
            self._errors['email'] = self.error_class([msg])  #afisez eroarea in interfata pe field-ul email


        #verificare stardate > endate
        get_start_date = cleaned_date.get('start_date')
        get_end_date = cleaned_date.get('end_date')

        if get_start_date > get_end_date:
            msg = "start date este mai mare decat end date"
            self._errors['start_date'] = self.error_class([msg])








# class Meta intr un proiect django este folosit pt a defini metadatele asociate cu un
#formular

#metadate-includ info dintr un model legat de formular, campurile care trebuiesc sa apara
#in formular si pe care le putem customiza adaugand clase de CSS, placeholder etc


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age','email','description',
                  'start_date', 'end_date', 'active','gender','trainer','profile']  #specific ce fields vreau in forms si ordinea lor


        widgets ={
            'first_name': TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Your first name'}),
            'last_name': TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your last name'}),
            'age': NumberInput(attrs={'class': 'form-control',"placeholder":"Enter your age"}),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Your email'}),
            'description': Textarea(attrs={"class":"form-control",'placeholder': 'Enter Your description', 'rows':3}),
            'start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),  # type -> datetime-local
            'end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),  # type -> datetime-local
            'gender': Select(attrs={'class': 'form-select'}),
            'trainer': Select(attrs={'class':'form-select'})
        }