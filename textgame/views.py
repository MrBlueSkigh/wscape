from django.http import HttpResponse
from django.shortcuts import render
from django.views import generic
from django.template import loader
from .models import Room, Player
from .forms import LoadPlayer, CreatePlayer
from .weatherscraper import WeatherScraper

def StartingScreen(request):
    return render(request, 'textgame/start.html', {})

class genericRoom(generic.DetailView):
    model = Room
    template_name = "textgame/room.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ws = WeatherScraper()
        context['weather'] = ws.getData()
        return context

class LoginScreen(generic.FormView):
    template_name = "textgame/login.html"
    form_class = CreatePlayer
    success_url = "/1/"

class LoadScreen(generic.FormView):
    template_name = "textgame/login.html"
    form_class = LoadPlayer
    success_url = "/1/"
    
