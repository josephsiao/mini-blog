from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render

from .form import UserLoginForm, UserRegistrationForm


def index(request):
    return render(request, 'home/index.html')


def user_register(request):
    if request.user.is_authenticated:
        messages.info(request, '你已註冊且登入中')

        return redirect('/')

    redirect_to = request.GET.get('next', '')

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, '註冊成功')

            return redirect(redirect_to) if redirect_to else redirect('/')
        else:
            context = {
                'form': form,
                'next': redirect_to
            }

            return render(request, 'registration/register.html', context)
    else:
        form = UserRegistrationForm()

        context = {
            'form': form,
            'next': redirect_to
        }

        return render(request, 'registration/register.html', context)


def user_login(request):
    if request.user.is_authenticated:
        messages.info(request, '你已登入')

        return redirect('/')

    redirect_to = request.GET.get('next', '')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            messages.success(request, '你已成功登入')

            return redirect(redirect_to) if redirect_to else redirect('/')

    form = UserLoginForm()

    context = {
        'form': form,
        'next': redirect_to
    }

    return render(request, 'registration/login.html', context)


def user_logout(request):
    redirect_to = request.GET.get('next', '')
    logout(request)

    messages.success(request, '你已成功登出')

    return redirect(redirect_to) if redirect_to else redirect('/')
