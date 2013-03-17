from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'team.views.home', name='home'),
    #url(r'^$', 'team.views.home', name='team'),
    url(r'^$', 'team.views.home', name='team_home'),
    url(r'^team/$', 'team.views.team', name='team_team'),
    url(r'^team/(?P<pk>\d+)$', 'team.views.team', name='team_team'),
    url(r'^players/(?P<pk>\d+)$', 'team.views.players', name='team_players'),
    # url(r'^basketball/', include('basketball.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


)
