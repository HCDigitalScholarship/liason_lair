from django.db import models

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
