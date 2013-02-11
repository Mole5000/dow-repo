# Create your views here.

from django.utils import simplejson
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, render, redirect
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

def save_history(request, pk):
    print "Saving", pk
    hist_obj = History.objects.get(pk=pk)
    hist_obj.description = request.POST["text_input"]; 
    hist_obj.save()
    request.POST["text_input"]   
    return redirect("/gazateer/history/"+pk)

