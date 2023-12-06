from django.urls import path

from materials.apps import MaterialsConfig
from materials.views import MaterialCreateView

app_name = MaterialsConfig.name

urlpatterns = [
    path('create/', MaterialCreateView.as_view(), name='create'),
    # path('', ..., name='list'),
    # path('view/<int:pk>', ..., name='view'),  # detail?
    # path('edit/<int:pk>', ..., name='edit'),
    # path('delete/<int:pk>', ..., name='delete'),
]
