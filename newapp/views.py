from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
import datetime
from newapp.models import Course
import random
from .forms import ContactForm, QuestionForm
# Create your views here.


def index(request):
    now = datetime.datetime.now()
    return render(request, 'index.html', {'current_date': now})
    #now = datetime.datetime.now()
    #t = get_template('index.html')
    #html = t.render({'current_date': now})
    #return HttpResponse(html)

    #return render(request, 'index.html', {})

def research(request):
        return render(request, 'research.html',{})
    
def addquestion(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form2.is_valid():
            question = form.cleaned_data['question']
            details = form.cleaned_data['details']
            category = form.cleaned_data['category']
    form = QuestionForm()
    return render(request, 'addquestion.html',{'form':form})

def about(request):
    return render(request, 'about.html',{})

def faq(request):
    return render(request, 'faq.html',{})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            category = form.cleaned_data['category']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']

    form = ContactForm()
    return render(request, 'contact.html',{'form':form})

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
