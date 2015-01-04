from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Happening

class HappeningListView(generic.ListView):
	model = Happening
	template_name = 'happenings/happening_list.html'

class HappeningDetailView(generic.DetailView):
	model = Happening
	template_name = 'happenings/happening_detail.html'