from django.shortcuts import render
from django.views.generic import ListView
from ch4.models import Page
# Create your views here.
class Homepageview(ListView):
    model = Page
    template_name = 'ch4/home_list.html'
    context_object_name = 'home_page'