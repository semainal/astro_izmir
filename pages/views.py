from django.shortcuts import render
from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class EvlerPageView(TemplateView):
    template_name = 'evler.html'

class GezegenlerPageView(TemplateView):
    template_name = 'gezegenler.html'

class AcilarPageView(TemplateView):
    template_name = 'acilar.html'

class TransitlerPageView(TemplateView):
    template_name = 'transitler.html'

class HakkindaPageView(TemplateView):
    template_name = 'hakkinda.html'

class ElementlerPageView(TemplateView):
    template_name = 'elementler.html'

class BurclarPageView(TemplateView):
    template_name = 'burclar.html'

# Create your views here.
