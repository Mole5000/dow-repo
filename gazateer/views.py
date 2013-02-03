# Create your views here.

from django.utils import simplejson
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from gazateer.models import History, Race
import markdown

def format_for_screen(markdown_text):
    return markdown.markdown(markdown_text)

def list_of_things(request):
    things = []
    for race in Race.objects.all():
        things.append({'name':race.wiki_name()})
    
    return HttpResponse(simplejson.dumps(things), mimetype="application/json")

def crap(request):
    return render(request, 'example.html', {})

