from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.urls import reverse_lazy

# Create your views here.

class LoginView(TemplateView):
    template_name = 'users/login.html'
    success_url = '/'  # Redirect to home page after successful login
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Login Page'
        return context
    
    def post(self, request, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            # Successful authentication -> log in and redirect
            login(self.request, user)
            return redirect(self.success_url)
        else:
            message = "Invalid username or password"
            return render(request, self.template_name, {'message': message})
    
    
class RegisterView(CreateView):
    # Use Django's UserCreationForm to ensure password hashing and validation
    form_class = UserCreationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('login_view')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register Page'
        return context
    
class LogoutView(View):
    success_url = '/'  # Redirect to home page after logout
    
    def get(self, request):
        logout(request)
        return redirect('life_time_view')