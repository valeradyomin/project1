from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.models import Student


# Create your views here.

class StudentsListView(ListView):
    model = Student
    # template_name = 'main/student_list.html'


class StudentDetailView(DetailView):
    model = Student
    # template_name = 'main/student_detail.html'


class StudentCreateView(CreateView):
    model = Student
    fields = ('first_name', 'last_name', 'avatar',)
    success_url = reverse_lazy('main:index')


class StudentUpdateView(UpdateView):
    model = Student
    fields = ('first_name', 'last_name', 'avatar',)
    success_url = reverse_lazy('main:index')


class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('main:index')


def index(request):
    students_list = Student.objects.all()
    context = {
        'object_list': students_list,
        'title': 'Главная страница'
    }
    return render(request, 'main/student_list.html', context)


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'{name} - {email}: {message}')

    context = {
        'title': 'Контакты'
    }
    return render(request, 'main/contact.html', context)


def student(request, pk):
    student_item = Student.objects.get(id=pk)
    context = {
        'object': student_item,
        'title': f'студент - {student_item.first_name.title()} {student_item.last_name.title()}'
    }
    return render(request, 'main/student_detail.html', context=context)
