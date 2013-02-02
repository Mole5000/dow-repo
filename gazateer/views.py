# Create your views here.

import markdown
from django.shortcuts import render_to_response
from gazateer.models import History
from django.http import HttpResponse

def format_for_screen(markdown_text):
    return markdown.markdown(markdown_text)

def complete_history():
    render_to_response("history_list.html",{"history":History.objects})
    
def edit_history(request,history_id):
    print history_id, "***"
    return HttpResponse()