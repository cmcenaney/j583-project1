# Create your views here.

from django.shortcuts import render
from team.models import Team, Players
from django.shortcuts import render, get_object_or_404, redirect, render_to_response


def home(request):
	context = {
		'players_count': Players.objects.count(),
		'team_count': Team.objects.count(),

	}
	return render(request, "team/home.html", context)


def team(request, pk):
	tempteams = Team.objects.get(id=pk)
	tempteams = tempteams.players.all() 
	team = get_object_or_404(Team, id=pk)
	context = {
		'teamList': tempteams,
		'team': team,
	}

	return render (request, "team/team.html", context)

def players(request, pk):
	players = get_object_or_404(Players, id=pk)
	return render (request, "team/players.html", {'players': players})