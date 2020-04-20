from django.contrib.auth.forms import UserCreationForm
# from django.http import HttpResponse
from django.shortcuts import redirect, render

from .form import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            if request.GET['next']:
                return redirect(request.GET['next'])
            else:
                return redirect('/')
        else:
            return render(request, 'registration/register.html', {'form': form})
    else:
        form = UserRegistrationForm()

        context = {
            'form': form
        }

        return render(request, 'registration/register.html', context)
