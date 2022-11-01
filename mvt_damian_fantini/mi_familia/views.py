from django.shortcuts import render
from datetime import date, datetime
from multiprocessing import context
from django.http import HttpResponse
from django.urls import re_path
from django.template import Template, Context, loader
from .models import MiFamilia


def mi_familia(request):
    familia = MiFamilia.objects.all()

    return render ( request, "mi_familia.html", {'familia': familia} )
    