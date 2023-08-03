from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView
from app.models import *


class teacher_list(ListView):
    model=Teacher

    template_name='teacher_list.html'
    context_object_name='tl'

    queryset=Teacher.objects.filter(tname='varun')
    #ordering=['tname']


    

