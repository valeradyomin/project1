from django import forms

from main.models import Student, Subject


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        # fields = '__all__'
        fields = ('first_name', 'last_name', 'avatar',)
        # exclude = ('last_name',)


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = '__all__'
        # fields = ('title', 'description',)

