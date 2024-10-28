from django.shortcuts import render
from .models import merch
# Create your views here.
def listadomerca(request):
    listademerch=merch.objects.all()
    return render(request, 'gestmerca.html',{"mimerca":listademerch})