from django.urls import path

from main.apps import MainConfig
from main.views import index, contact, student, StudentsListView, StudentDetailView

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('', StudentsListView.as_view(), name='index'),
    path('contact/', contact, name='contact'),
    path('student/<int:pk>', StudentDetailView.as_view(), name='student'),
    # path('student/<int:pk>', student, name='student'),
]
