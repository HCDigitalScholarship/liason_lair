from django.db import models
from datetime import datetime
#from django.contrib.auth.models import User
# Create your models here.


class Course(models.Model):
    campus = models.CharField(max_length=200, help_text='Campus')
    semester = models.CharField(max_length=200, help_text='Semester')
    title = models.CharField(max_length=200, help_text='Title')
    credit = models.CharField(max_length=200, help_text='Credit')
    department = models.CharField(max_length=200, help_text='Department')
    instructor = models.CharField(max_length=200, help_text='Instructor')
    times = models.CharField(max_length=200, help_text='Times')
    room = models.CharField(max_length=200, help_text='Times')
    additional_info = models.TextField()
    misc_links = models.TextField()

    def __str__(self):
        return self.title

class Question(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.CharField(max_length=140, help_text='Question')
    details = models.CharField(max_length=3000, help_text='Question Details', default='SOME STRING')
    tags = models.ManyToManyField('Tag')
    #pub_date = models.DateTimeField('date published', default = 'DATE')
    pass

class Tag(models.Model):
    tag = subtags = models.CharField(max_length=140, blank=True, null=True)
    subtags = models.ManyToManyField('Subtag')

class Subtag(models.Model):
    subtags = models.CharField(max_length=140)


class Answer(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    #question = models.ManyToManyField(Question)
    question = models.CharField(max_length=140, help_text='Question', default='Question default string')
    answer_text = models.CharField(max_length=3000, help_text='Answer Text')
    pub_date = models.DateTimeField('date published')

#<<<<<<< HEAD

# We should probably  extend the User model Django has already
# Django has name fields, so if we extend Django User model, we don't need those
# class User(models.Model):
#     class_year = models.CharField(max_length=20, help_text='Class Year')
#     class_year_choices = [
#         ('FR', 'Freshman'),
#         ('SO', 'Sophomore'),
#         ('JR', 'Junior'),
#         ('SR', 'Senior'),
#         ('GR', 'Graduate'),
#     ]
#     first_name = models.CharField(max_length=50, help_text='First Name')
#     last_name = models.CharField(max_length=100, help_text='Last Name')
#
#
#     def __str__(self):
#         return self.first_name + " " + self.last_name

#
#
# =======
# >>>>>>> db7b17e56787ea97de8358d75c1f0d40dce48f60
class Category(models.Model):
        name = models.CharField(max_length=100, help_text='Category Name')
