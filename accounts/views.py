# Create your views here.
from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import RegisterUserForm, LoginUserForm


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('book_list')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'accounts/login.html'


def logout_user(request):
    logout(request)
    return redirect('login')
