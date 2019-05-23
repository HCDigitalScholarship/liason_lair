from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.


class Course(models.Model):
    campus = models.CharField(max_length=20, help_text='Campus')
    semester = models.CharField(max_length=20, help_text='Semester')
    title = models.CharField(max_length=20, help_text='Title')
    credit = models.CharField(max_length=20, help_text='Credit')
    department = models.CharField(max_length=20, help_text='Department')
    instructor = models.CharField(max_length=20, help_text='Instructor')
    times = models.CharField(max_length=20, help_text='Times')
    room = models.CharField(max_length=20, help_text='Times')
    additional_info = models.CharField(max_length=20, help_text='Additional Info')
    misc_links = models.CharField(max_length=20, help_text='Misc. Links')

    def __str__(self):
        return self.title

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=140, help_text='Question')
    details = models.CharField(max_length=3000, help_text='Question Details')
    pub_date = models.DateTimeField('date published')
    pass

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ManyToManyField(Question)
    answer_text = models.CharField(max_length=3000, help_text='Answer Text')
    pub_date = models.DateTimeField('date published')
