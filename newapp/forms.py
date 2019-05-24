from django import forms
from newapp.models import Course

class CourseForm(forms.Form):
    class Meta:
        model = Course

class SearchForm(forms.Form):
	search = forms.CharField(label='search', max_length=100)

class QAForm(forms.Form):
    question = forms.CharField(label='question', max_length=140)
    answer = forms.CharField(label='Answer', max_length=3000)
