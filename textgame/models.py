from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
	room_name = models.CharField(max_length=50,default="")
	room_desc = models.CharField(max_length=500,default="")
	room_c1 = models.CharField(max_length=1000, default="")
	room_c2 = models.CharField(max_length=1000, default="")
	room_c3 = models.CharField(max_length=1000, default="")
	room_c1_a = models.CharField(max_length=5, default="")
	room_c2_a = models.CharField(max_length=5, default="")
	room_c3_a = models.CharField(max_length=5, default="")
	room_choiceCount = models.IntegerField(blank=True, null=True)
	room_type = models.IntegerField(blank=True, null=True)
	room_desc_alt = models.CharField(max_length=500,default="")
	room_back = models.CharField(max_length=20,default="")


	def __str__(self): 
		return self.room_name

class Player(models.Model):
	player_name = models.CharField(max_length=20,default="")
	player_pass = models.CharField(max_length=20,default="")
	player_lvl = models.CharField(max_length=50,default="")
	
	def __str__(self):
		return self.player_name


class Hash(models.Model):
	hash_hex = models.CharField(max_length=64,default="")

	def __str__(self):
		return self.hash_hex

