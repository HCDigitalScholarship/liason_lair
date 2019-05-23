from django import forms
from newapp.models import Course

class CourseForm(forms.Form):
    class Meta:
        model = Course

class SearchForm(forms.Form):
	search = forms.CharField(label='search', max_length=100)