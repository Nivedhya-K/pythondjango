from django.http import HttpResponse
from django.shortcuts import render
from . models import Cakes
from .models import Place
# Create your views here.
def demo(request):
    obj=Cakes.objects.all()
    obj1=Place.objects.all()
    return render(request,"index1.html",{'result':obj,'results':obj1})
