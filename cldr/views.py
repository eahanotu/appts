# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Appts
from .forms import ApptForm
from django.core import serializers


def index(request):
    if request.method == "POST":        
        form = ApptForm(request.POST)
        if form.is_valid():
            new = Appts(date=request.POST['date'], time=request.POST['time'], description=request.POST['desc'])
            new.save()
            form = ApptForm() 
    else:
        form = ApptForm()
    #qs = Appts.objects.all()
    return render(request, 'index.html', {'form':form})

def getAppts(request):
    if request.POST.get('search', '') == '':
        qs = Appts.objects.all()
    else:
        qs = Appts.objects.filter(description = request.POST['search'])
    
    data = serializers.serialize("json", qs)
    
    return HttpResponse(data, content_type='application/json')
