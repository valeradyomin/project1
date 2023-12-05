from django.shortcuts import render
from django.views.generic import ListView, DetailView

from main.models import Students


# Create your views here.

class StudentsListView(ListView):
    model = Students
    template_name = 'main/index.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     print(context)
    #     return context


class StudentDetailView(DetailView):
    model = Students
    template_name = 'main/student.html'


def index(request):
    students_list = Students.objects.all()
    context = {
        'objects_list': students_list,
        'title': 'Главная страница'
    }
    return render(request, 'main/index.html', context)


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
    student_item = Students.objects.get(id=pk)
    context = {
        'object': student_item,
        'title': f'студент - {student_item.first_name.title()} {student_item.last_name.title()}'
    }
    return render(request, 'main/student.html', context=context)
