from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from .forms import RegisterForm, LoginForm  # Assuming you're using custom forms, otherwise use Django's built-in forms.

# Register view
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()  # Save the user to the database
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('login')  # Redirect to login page
    else:
        form = RegisterForm()  # Empty form for GET request
    
    return render(request, 'register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You have successfully logged in.')
                return redirect('home')  # Redirect to homepage or desired page
            else:
                messages.error(request, 'Invalid login credentials. Please try again.')
    else:
        form = LoginForm()  # Empty form for GET request

    return render(request, 'login.html', {'form': form})

# Logout view
def logout_view(request):
    logout(request)  # Logout the current user
    messages.success(request, 'You have successfully logged out.')
    return redirect('home')  # Redirect to homepage after logout
