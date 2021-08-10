from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegisterForm, MLERegisterForm
from django.contrib.auth.decorators import login_required
from users.models import CustomUser
from .genpassword import generatePassword
# Create your views here.


def CreateUser(request):
    return CustomUser.objects.create(
        username=request.POST['username'],
    )


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
            # [1]: Create User
            manager = CreateUser(request)

            # [2]: Assign Password
            password = generatePassword()
            manager.set_password(password)

            # [3]: Define Type
            manager.is_manager = True

            # [4]: Deactivate Account && save
            # gamma.is_active = False
            manager.save()

            #TODO: 
            # # [5]: Send Email
            # ActivationMailer(recipient_list=zeta.email).send_email()

            # [6]: redirect
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
            # [1]: Create User
            editor = CreateUser(request)

            # [2]: Assign Password
            password = generatePassword()
            editor.set_password(password)

            # [3]: Define Type
            editor.is_editor = True

            # [4]: Deactivate Account && save
            # gamma.is_active = False
            editor.save()

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
