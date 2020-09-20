from django.contrib import admin

from .models import PlayerGameInfo, Game, Player

admin.site.register(PlayerGameInfo)
admin.site.register(Game)
admin.site.register(Player)
