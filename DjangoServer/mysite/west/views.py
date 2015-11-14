# -*- coding: utf-8 -*-
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from west.models import Character

def staff(request):
	staff_list = Character.objects.all()
	#staff_str = map(str, staff_list)
	#context = {'label' : ' '.join(staff_str)}
	return render(request, 'templay.html', {'staffs': staff_list})

def templay(request):
	context = {}
	context['label'] = 'Hello World!'
	return render(request, 'templay.html', context)
