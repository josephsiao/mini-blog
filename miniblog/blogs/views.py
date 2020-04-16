from datetime import datetime

# from django.http import HttpResponse
from django.shortcuts import render
# from django.views.generic.base import TemplateView


def index(request):
    # return HttpResponse(str(datetime.now()))
    return render(request, 'index.html', {
        'current_time': str(datetime.now()),
    })
