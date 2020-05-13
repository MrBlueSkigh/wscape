from django.forms import ModelForm, Form
from .models import Player

class LoadPlayer(ModelForm):
    
    class Meta:
        model = Player
        fields = ['player_name','player_pass','player_lvl']

class CreatePlayer(ModelForm):
    
    class Meta:
        model = Player
        fields = ['player_name','player_pass']