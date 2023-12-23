from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, ProfileView, MyLoginView

app_name = UsersConfig.name

urlpatterns = [
    # existed default controller
    path('', MyLoginView.as_view(template_name='users/login.html'), name='login'),
    # existed default controller
    path('logout/', LogoutView.as_view(), name='logout'),
    # controller need create manually from generics
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
]