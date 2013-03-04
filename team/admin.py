from django.contrib import admin
from team.models import Team, Players

class TeamAdmin(admin.ModelAdmin):
    search_fields = ('name',)

admin.site.register(Team, TeamAdmin)

class PlayersAdmin(admin.ModelAdmin):
    search_fields = ('name',),
    
admin.site.register(Players, PlayersAdmin) 