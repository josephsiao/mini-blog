from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime


def index(request):
    return HttpResponse(str(datetime.now()))
