from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ihc_game.views.home', name='home'),

    url(r'^analizar/?$', "ihc_game.views.analizar", name="analizar"),

    # url(r'^blog/', include('blog.urls')),


    url(r'^admin/', include(admin.site.urls)),
)
