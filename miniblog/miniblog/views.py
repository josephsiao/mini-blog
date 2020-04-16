from django.contrib.auth.forms import UserCreationForm
# from django.http import HttpResponse
from django.shortcuts import redirect, render


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'registration/register.html', {'form': form})
    else:
        form = UserCreationForm()

        context = {
            'form': form
        }

        return render(request, 'registration/register.html', context)
