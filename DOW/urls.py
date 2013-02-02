from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from gazateer.models import History
from django.views.generic.list import ListView
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #    url(r'^DOW', ListView.as_view(
    #            queryset=History.objects.all(),
    #            context_object_name='latest_history_list',
    #            template_name='index.html'),
    #        name='index'),
    url(r'^gazateer/', include('gazateer.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
