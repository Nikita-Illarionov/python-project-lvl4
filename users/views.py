from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, UpdateView, DeleteView
from django.urls import reverse
from .models import CustomUser
from django.db import models
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin




def user_table(request):
    users = CustomUser.objects.all()
    
    return render(request, 'users/main.html', {'users': users})




class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CustomUser
    template_name = 'users/update.html'
    form_class = RegisterForm
    success_url = '/users/'
    login_url = 'users'
    
    def test_func(self):
        obj = self.get_object()
        return obj == self.request.user

    def handle_no_permission(self):
        return redirect(self.login_url)




class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CustomUser
    template_name = 'users/delete.html'
    success_url = '/users/'
    login_url = 'users'
    error_url = '/users/'

    def test_func(self):
        obj = self.get_object()
        return obj == self.request.user

    def handle_no_permission(self):
        return redirect(self.login_url)


    def get_error_url(self):
        if self.error_url:
            return self.error_url.format(**self.object.__dict__)
        else:
            raise ImproperlyConfigured(
               "No error URL to redirect to. Provide a error_url.")

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect. 
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        error_url = self.get_error_url()
        try:
             self.object.delete()
             return HttpResponseRedirect(success_url)
        except models.ProtectedError:
             return HttpResponseRedirect(error_url)




class RegisterView(FormView):
    form_class = RegisterForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "users/create.html"

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()
        messages.success(self.request, 'Пользователь успешно зарегистрирован')

        # Вызываем метод базового класса
        return super(RegisterView, self).form_valid(form)



# Опять же, спасибо django за готовую форму аутентификации.
from django.contrib.auth.forms import AuthenticationForm

# Функция для установки сессионного ключа.
# По нему django будет определять, выполнил ли вход пользователь.
from django.contrib.auth import login

class LoginView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "users/login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        messages.success(self.request, 'Вы залогинены')
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginView, self).form_valid(form)


from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout


class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)
        messages.info(self.request, 'Вы разлогинены')

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/")
