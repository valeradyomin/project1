from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from main.forms import StudentForm, SubjectForm
from main.models import Student, Subject


# Create your views here.

class StudentsListView(ListView):
    model = Student
    # template_name = 'main/student_list.html'


class StudentDetailView(DetailView):
    model = Student
    # template_name = 'main/student_detail.html'


class StudentCreateView(CreateView):
    model = Student
    # OLD
    # fields = ('first_name', 'last_name', 'avatar',)
    success_url = reverse_lazy('main:index')
    # -> NEW
    # add StudentForm
    form_class = StudentForm


class StudentUpdateView(UpdateView):
    model = Student
    success_url = reverse_lazy('main:index')
    form_class = StudentForm

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Student, Subject, form=SubjectForm, extra=1)
        if self.request.method == 'POST':
            # instance=self.object - только для редактирования указываем, при создании нет
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            # instance=self.object - только для редактирования указываем, при создании нет
            context_data['formset'] = SubjectFormset(instance=self.object)
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)


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


def toggle_activity(request, pk):
    student_item = get_object_or_404(Student, pk=pk)
    if student_item.is_active:
        student_item.is_active = False
    else:
        student_item.is_active = True

    student_item.save()

    return redirect(reverse('main:index'))
