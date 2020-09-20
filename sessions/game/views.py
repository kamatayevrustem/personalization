from django.shortcuts import render, redirect, HttpResponseRedirect
from collections import Counter
from django.core.exceptions import ObjectDoesNotExist

import random

import django.utils
from .models import PlayerGameInfo, Game, Player
from django.utils import timezone




def show_home(request):

    context = {'secret_number': '0',
               }

    if not request.session.session_key:
        request.session.save()
    session_id = request.session.session_key

    # check if there is no active game, then create
    if not(bool(Game.objects.filter(active=True))):
        game_data = start_game(request)
        new_game = game_data['game']
        creator = game_data['player']
        context['secret_number'] = new_game.secret_number
        template = 'game_stats.html'


    # if there is active game in place, then define player (or create)
    else:
        request.session['has_session'] = True
        try:
            player = Player.objects.get(session_id = request.session.session_key)
        except ObjectDoesNotExist:
            player = Player.objects.create(session_id=request.session.session_key)

        existing_game = Game.objects.filter(active=True).latest('pk')
        context['secret_number'] = existing_game.secret_number

        # print(existing_game.creator.session_id)
        if player.session_id == existing_game.creator.session_id:
            template = 'game_stats.html'
            context['attempts'] = PlayerGameInfo.objects.filter(game=existing_game, guess=True).count()

        else:
            template = 'home.html'
            context['advice'] = ""

            if request.POST.get('guess_number'):
                request.session['has_session'] = True

                picked_number = int(request.POST.get('guess_number'));
                print(request.POST.get('guess_number'))
                guess = PlayerGameInfo.objects.create(game = existing_game, guess = True, time = django.utils.timezone.now())

                if picked_number > existing_game.secret_number:
                    context['advice'] = "Загаданное число ниже"
                elif picked_number < existing_game.secret_number:
                    context['advice'] = "Загаданное число выше"
                else:
                    context['advice'] = "Вы угадали! Загаданное число - {0}".format(existing_game.secret_number)
                    # existing_game= False
                    id = existing_game.pk
                    Game.objects.filter(pk=id).update(active=False)

    return render(
        request,
        template,
        context=context
    )



def start_game(request):

    # if request.POST.get('set_number'):
    #     secret_number = request.POST.get('set_number')
    #     # print(game)
    #     try:
    #         player = Player.objects.get(session_id = request.session.session_key)
    #     except ObjectDoesNotExist:
    #         player = Player.objects.create(session_id = request.session.session_key)
    #     game = Game.objects.create(secret_number=secret_number, active=True, creator = player)
    #     player_action = PlayerGameInfo.objects.create(game=game, guess=False, time=django.utils.timezone.now())

    try:
        player = Player.objects.get(session_id=request.session.session_key)
    except ObjectDoesNotExist:
        player = Player.objects.create(session_id = request.session.session_key)
    secret_number = random.randint(1, 100)
    game = Game.objects.create(secret_number=secret_number, active=True, creator=player)
    player_action = PlayerGameInfo.objects.create(game=game, guess=False, time=django.utils.timezone.now())

    context = dict(game=game, player=player)

    return context

def guess_number(request):
    pass