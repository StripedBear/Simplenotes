from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import login, authenticate 
from simplenotes.users.forms import UserRegistrationForm
from django.contrib.auth.models import User


class SignUp(View):
    def get(self, request, *args, **kwargs):
        form = UserRegistrationForm()
        return render(request, 'registration/register.html', {'form': form})
        
    def post(self, request, *args, **kwargs):
        form = UserRegistrationForm(request.POST) 
        if form.is_valid(): 
            user = form.save() 
            login(request, user)
            return redirect('notes')
        return render(request, 'registration/register.html', {'form': form, 'errors': form.errors})
    

def home(request):
    return render(request, "home/home.html")
    
