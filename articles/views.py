from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.db.models import fields
from django.views.generic import ListView,DetailView,CreateView

from django.urls import reverse_lazy
from .models import Article

class ArticleListView(LoginRequiredMixin,ListView):
    model = Article
    template_name = "article_list.html"
    login_url = 'login'

class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = Article
    template_name = "article_detail.html"
    login_url = 'login'

# Create your views here.
