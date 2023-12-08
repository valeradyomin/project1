from django.contrib import admin

from main.models import Student

# Register your models here.

# вариант — самый простой и быстрый
# admin.site.register(Students)


@admin.register(Student)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ('first_name', 'last_name',)
