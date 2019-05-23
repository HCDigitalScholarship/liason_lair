from django import forms
from newapp.models import Course

class CourseForm(forms.Form):
    class Meta:
        model = Course

class SearchForm(forms.Form):
	search = forms.CharField(label='search', max_length=100)

class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label='e-mail')
    category = forms.ChoiceField(choices=[('suggestions', 'Suggestions'), ('question', 'Question'), ('report error', 'Report Error'), ('other', 'Other')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)
    
