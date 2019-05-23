from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
import datetime
from newapp.models import Course
import random
# Create your views here.


def index(request):
    now = datetime.datetime.now()
    return render(request, 'index.html', {'current_date': now})
    #now = datetime.datetime.now()
    #t = get_template('index.html')
    #html = t.render({'current_date': now})
    #return HttpResponse(html)

    #return render(request, 'index.html', {})

def course(request):
    now = datetime.datetime.now()
    course = Course.objects.all()
    random_course = random.choice(course)

    return render(request, 'index.html', {'course': random_course, 'current_date': now})

def department(request, department):
    now = datetime.datetime.now()
    course = Course.objects.filter(department=department)
    random_course = random.choice(course)

    return render(request, 'index.html', {'course': random_course, 'current_date': now})

def semester(request, semester):
    now = datetime.datetime.now()
    course = Course.objects.filter(semester=semester)
    random_semester = random.choice(semester)

    return render(request, 'index.html', {'semester': random_semester, 'current_date': now})
