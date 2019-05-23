from django import forms
from newapp.models import Course

class CourseForm(forms.Form):
    class Meta:
        model = Course
