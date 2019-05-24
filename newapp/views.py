from django.shortcuts import render
from django.template.loader import get_template
from django.http import HttpResponse
import datetime
from newapp.models import Course
import random
from .forms import QAForm
# Create your views here.


def index(request):
    now = datetime.datetime.now()
    if request.method == 'POST':
        print("we got to post")
        form = QAForm(request.POST)
        #search_form = SearchForm(request.POST)

        if form.is_valid() :
            question = request.POST.get('question', None)
            #search_query = request.POST.get('search', None)
            return render(request, 'index.html', {'current_date': now, 'question': question})

        return render(request, 'index.html', {'current_date': now})
    return render(request, 'index.html', {'current_date': now})

def contact(request):
    now = datetime.datetime.now()
    return render(request, 'contact.html', {'current_date': now})

def faq(request):
    now = datetime.datetime.now()
    return render(request, 'faq.html', {'current_date': now})


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
