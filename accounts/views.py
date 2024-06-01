from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from .forms import CustomUserCreationForm
import logging
from firebase_admin import firestore
from personal_assignments.authorization import try_login
from personal_assignments.web_service import save_user
from personal_assignments.cookie import getTheme
from personal_assignments.data_layer import get_books

logger = logging.getLogger(__name__)
db = firestore.client()

def register(request):
    theme=getTheme(request)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        value = save_user(form)
        if value:
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', 
                  {'form': form , 'theme':theme})

def login_view(request):
    theme=getTheme(request)
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        value = try_login(email, password, request)
        if value:
            return redirect('home')
    return render(request, 'accounts/login.html' ,
                  {'theme':theme})

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')

def home(request):
    theme=getTheme(request)
    books_data=get_books()   
    return render(request, 'home.html', 
                  {'books': books_data, 'theme':theme})

