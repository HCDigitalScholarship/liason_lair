from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
import datetime
from newapp.models import Course, Question, Answer
import random
from .forms import ContactForm, QuestionForm, Qform
# Create your views here.


def index(request):
    now = datetime.datetime.now()
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Qform(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            question = form.cleaned_data['question']
            details = form.cleaned_data['details']
            q = Question(question = question, details = details)
            q.save()
            return HttpResponse('Thanks')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Qform()
    # all_questions = Question.objects.all();
    # print(all_questions)
    #return render(request, 'index.html', {'form': form}, {'all_questions': all_questions})
    return render(request, 'index.html', {'form': form})


def contact(request):
    now = datetime.datetime.now()
    return render(request, 'contact.html', {'current_date': now})

def faq(request):
    now = datetime.datetime.now()
    return render(request, 'faq.html', {'current_date': now})


def research(request):
    return render(request, 'research.html',{})

def addquestion(request):
    if request.method == 'POST':
        form = Qform(request.POST)
        if form.is_valid():
            question = form.cleaned_data['question']
            details = form.cleaned_data['details']
            q = Question(question = question, details = details)
            q.save()
            return HttpResponse('Thanks')
        else:
            form = Qform()
            return render(request, 'addquestion.html', {'form': form})
    form = Qform()
    all_questions = Question.objects.all()
    all_answers= Answer.objects.all()
    return render(request, 'addquestion.html', {'form': form, 'all_questions' : all_questions, 'all_answers' : all_answers})

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

# def get_answer(request):
#     if request.method == 'POST':
#         form = QAForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect('/thanks/')
#     else:
#         form = NameForm()
#     return render(request, 'index.html', {'form': form})
