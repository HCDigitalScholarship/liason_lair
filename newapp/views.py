from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
import datetime

# Create your views here.


def index(request):
    now = datetime.datetime.now()
    return render(request, 'index.html', {'current_date': now})
    #now = datetime.datetime.now()
    #t = get_template('index.html')
    #html = t.render({'current_date': now})
    #return HttpResponse(html)
    
    #return render(request, 'index.html', {})
