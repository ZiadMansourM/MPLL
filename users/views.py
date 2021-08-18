from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegisterForm, MLERegisterForm
from django.contrib.auth.decorators import login_required
from users.models import CustomUser
from .services.user_factory import (
    ManagerRegistrationStrategy,
    EditorRegistrationStrategy
    )
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, "Your Account has been Created! You are now able to Log In")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {"form": form})


@login_required
def registermanager(request):
    if request.method == "POST":
        form = MLERegisterForm(request.POST)
        if form.is_valid():
            password = ManagerRegistrationStrategy().create_user(username=request.POST['username'])

            #TODO: 
            # Send Email
            # ActivationMailer(recipient_list=zeta.email).send_email()

            # redirect
            messages.success(
                request, f'The manager user were added successfully, password: {password}')
            return redirect('profile')
    else:
        form = MLERegisterForm()

    context = {
        'form': form,
        'type': 'manager'
    }
    return render(request, 'users/register.html', context)


@login_required
def registereditor(request):
    if request.method == "POST":
        form = MLERegisterForm(request.POST)
        if form.is_valid():
            password = EditorRegistrationStrategy().create_user(username=request.POST['username'])

            #TODO: 
            # # [5]: Send Email
            # ActivationMailer(recipient_list=zeta.email).send_email()

            # [6]: redirect
            messages.success(
                request, f'The editor user were added successfully, password: {password}')
            return redirect('profile')
    else:
        form = MLERegisterForm()

    context = {
        'form': form,
        'type': 'editor'
    }
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    return render(request, 'users/profile.html')
