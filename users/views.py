from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView
from django.views.decorators.http import require_http_methods
from django.contrib.auth.mixins import UserPassesTestMixin
# email imports
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text

from .services.user_factory import (
    LibrarianRegistrationStrategy,
    NormalRegistrationStrategy,
    ManagerRegistrationStrategy,
    EditorRegistrationStrategy
)
from .services.mailers import ActivationMailer

from users.forms import (
    LibrarianRegisterForm,
    UserRegisterForm,
    MLERegisterForm,
    ProfileUpdateForm,
    LogInForm
)
# Create your views here.

User = get_user_model()


class MPLLLogin(UserPassesTestMixin, LoginView):
    form_class = LogInForm
    template_name = 'users/login.html'

    def test_func(self):
        return not self.request.user.is_authenticated


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            # [1]: create user
            username, user = NormalRegistrationStrategy().create_user(form)
            # [2]: send email
            ActivationMailer(get_current_site(
                request).domain, user).send_email()
            return HttpResponse(f'Please Mr/Ms {username} confirm your email address to complete the registration')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {"form": form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(
            request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('login')
    else:
        return HttpResponse('Activation link is invalid!')


def is_authenticated_as_manager(user):
    print("test")
    return user.is_manager


@login_required
@user_passes_test(is_authenticated_as_manager)
def registermanager(request):
    print(request.user)
    if request.method == "POST":
        form = MLERegisterForm(request.POST)
        if form.is_valid():
            # [1]: create user
            password, manager = ManagerRegistrationStrategy().create_user(form)
            # [2]: Send Email
            ActivationMailer(get_current_site(
                request).domain, manager).send_email()
            # [3]: redirect
            messages.success(
                request, f'The manager user was added successfully, password: {password}')
            return redirect('profile')
    else:
        form = MLERegisterForm()

    context = {
        'form': form,
        'type': 'manager'
    }
    return render(request, 'users/register.html', context)


@login_required
@user_passes_test(is_authenticated_as_manager)
def registerlibrarian(request):
    if request.method == "POST":
        form = LibrarianRegisterForm(request.POST)
        if form.is_valid():
            # [1]: create user
            password, librarian = LibrarianRegistrationStrategy().create_user(form)
            # [2]: Send Email
            ActivationMailer(get_current_site(
                request).domain, librarian).send_email()
            # [3]: redirect
            messages.success(
                request, f'The librarian user was added successfully, password: {password}')
            return redirect('blog-home')
    else:
        form = LibrarianRegisterForm()

    context = {
        'form': form,
        'type': 'librarian'
    }
    return render(request, 'users/register.html', context)


@login_required
@user_passes_test(is_authenticated_as_manager)
def registereditor(request):
    if request.method == "POST":
        form = MLERegisterForm(request.POST)
        if form.is_valid():
            # [1]: create user
            password, editor = EditorRegistrationStrategy().create_user(form)
            # [2]: Send Email
            ActivationMailer(get_current_site(
                request).domain, editor).send_email()
            # [3]: redirect
            messages.success(
                request, f'The editor user was added successfully, password: {password}')
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
    if request.method == "POST":
        form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user)  # request.FILES [2]
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Profile Has Been Updated')
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)
    context = {
        "form": form
    }
    return render(request, 'users/profile.html', context)


@login_required
@require_http_methods(["POST"])
def deactivate(request):
    user = request.user
    user.is_active = False
    user.save()
    return HttpResponse("Your account has been deactivated successfuly, hope to see you again soon!")
