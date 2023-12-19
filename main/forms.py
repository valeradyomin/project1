from django import forms

from main.models import Student, Subject


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        # fields = '__all__'
        fields = ('first_name', 'last_name', 'avatar', 'email',)
        # exclude = ('last_name',)

    # валидация форм
    def clean_email(self):
        cleaned_data = self.cleaned_data['email']

        if 'skypro' not in cleaned_data:
            raise forms.ValidationError('почта должна быть от домена "skypro"')

        return cleaned_data

    # стилизация форм
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'



class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = '__all__'
        # fields = ('title', 'description',)

    # стилизация форм
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

