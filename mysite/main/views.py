import datetime
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    current_datetime = datetime.datetime.now()
    current_datetime = current_datetime.strftime(f"рік {current_datetime.year} місяц {current_datetime.month} Число {current_datetime.day}")
  
    return render(request, 'main/index.html', {'a':current_datetime})

def pnev(request):
    return render(request, 'main/pnevmat2.html')

def trav2(request):
    return render(request, 'main/travmat2.html')

def tren(request):
    return render(request, 'main/trenyval.html')

def sig(request):
    return render(request, 'main/signal.html')

def stri(request):
    return render(request, 'main/strikeboll.html')

def pnev1(request):
    return render(request, 'main/pnevmat.html')

def flo(request):
    return render(request, 'main/flober.html')

def trav(request):
    return render(request, 'main/travmat.html')