from django.db import models

from datetime import datetime

class Player(models.Model):
    session_id = models.CharField(max_length=256)

class Game(models.Model):
    secret_number = models.IntegerField(default=0)
    active = models.BooleanField(default=False)
    creator = models.ForeignKey(Player, on_delete=models.CASCADE)

class PlayerGameInfo(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, default=0)
    guess = models.BooleanField(default=0)
    time = models.DateTimeField(default=datetime.now())
    # player = models.ForeignKey(Player, on_delete=models.CASCADE)

