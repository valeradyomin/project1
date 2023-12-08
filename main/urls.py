from django.urls import path

from main.apps import MainConfig
from main.views import index, contact, student, StudentsListView, StudentDetailView, StudentCreateView, \
    StudentUpdateView, StudentDeleteView, toggle_activity

app_name = MainConfig.name

urlpatterns = [
    # path('', index, name='index'),
    # path('student/<int:pk>', student, name='student'),
    path('', StudentsListView.as_view(), name='index'),
    path('student/<int:pk>', StudentDetailView.as_view(), name='student'),
    path('contact/', contact, name='contact'),
    path('create/', StudentCreateView.as_view(), name='create_student'),
    path('edit/<int:pk>/', StudentUpdateView.as_view(), name='edit_student'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='delete_student'),
    path('activity/<int:pk>/', toggle_activity, name='toggle_activity'),
]
