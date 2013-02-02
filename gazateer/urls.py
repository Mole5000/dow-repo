from django.conf.urls import patterns, url

from gazateer.models import History
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(
            queryset=History.objects.all(),
            context_object_name='latest_history_list',
            template_name='history_list.html'),
        name='index'),
    url(r'^history/(?P<pk>\d+)$', DetailView.as_view(
            model=History,
            template_name='history_detail.html'),
        name='detail'),
)