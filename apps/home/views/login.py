from typing import Any
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.urls import path, reverse


class CustomLoginView(LoginView):
    template_name = 'acesso/login.html'

    def get_success_url(self):
        return reverse('home')
    
    def form_invalid(self, form):
        return super().form_invalid(form)
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        return super().post(request, *args, **kwargs)
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse('home'))
        return super().get(request, *args, **kwargs)
    