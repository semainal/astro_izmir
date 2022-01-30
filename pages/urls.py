from django.urls import path
from .views import AcilarPageView, BurclarPageView, ElementlerPageView, EvlerPageView, GezegenlerPageView, HakkindaPageView, HomePageView, TransitlerPageView

urlpatterns = [ 
    path('',HomePageView.as_view(), name='home'),
    path('evler/', EvlerPageView.as_view(), name='evler'),
    path('gezegenler/', GezegenlerPageView.as_view(), name='gezegenler'),
    path('acilar/', AcilarPageView.as_view(), name='acilar'),
    path('transitler/', TransitlerPageView.as_view(), name='transitler'),
    path('hakkinda/', HakkindaPageView.as_view(), name='hakkinda'),
    path('elementler/', ElementlerPageView.as_view(), name='elementler'),
    path('burclar/', BurclarPageView.as_view(), name='burclar'),
]