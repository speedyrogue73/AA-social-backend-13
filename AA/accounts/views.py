from typing import Any

from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponseBase
from django.shortcuts import render, redirect
from django.views import View
from .forms import userregistrationForm, UserLoginForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin


class UserRegisterationView(View):
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponseBase:
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)
    def get(self, request):
        form = userregistrationForm()
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = userregistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your account has been created! You are now logged in.', 'success')
            return redirect('home:home')
        return render(request, 'accounts/register.html', {'form': form})



class UserLoginView(View):
    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponseBase:
        if request.user.is_authenticated:
            return redirect('home:home')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        form = UserLoginForm()
        return render(request, 'accounts/login.html', {'form': form})

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                request,
                phone_number=form.cleaned_data['phone_number'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                messages.success(request, 'You have been successfully logged in', 'success')
                return redirect('home:home')
            else:
                messages.error(request, 'Invalid Credentials', 'danger')
        return render(request, 'accounts/login.html', {'form': form})





class UserLogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        messages.success(request, 'You have been successfully logged out', 'success')
        return redirect('home:home')


