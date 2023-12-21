from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    # existed default controller
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    # existed default controller
    path('logout/', LogoutView.as_view(), name='logout'),
    # controller need create manually
    path('register/', RegisterView.as_view(), name='register'),
]