from django.urls import path

from main.apps import MainConfig
from main.views import index, contact, student

app_name = MainConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('student/<int:pk>', student, name='student'),
]
