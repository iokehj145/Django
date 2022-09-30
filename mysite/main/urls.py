from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.index),
  path('index.html', views.index),
  path('pnevmat2.html', views.pnev),
  path('travmat2.html', views.trav2),
  path('trenyval.html', views.tren),
  path('signal.html', views.sig),
  path('strikeboll.html', views.stri),
  path('pnevmat.html', views.pnev1),
  path('flober.html', views.flo),
  path('travmat.html', views.trav)
]