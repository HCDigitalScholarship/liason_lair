from django import forms
from newapp.models import Course, Category, Question
from crispy_forms.helper import FormHelper
from django.forms import ModelForm
from crispy_forms.layout import Layout, Submit

class CourseForm(forms.Form):
    class Meta:
        model = Course

class SearchForm(forms.Form):
	search = forms.CharField(label='Search', max_length=100)

class AnswerForm(forms.Form):
	answer = forms.CharField(label='Answer', max_length=1000, widget=forms.Textarea(attrs={"rows":5, "cols":40}))

#<<<<<<< HEAD
class Qform(ModelForm):
    question = forms.CharField(label='Question', max_length=1000, widget=forms.Textarea(attrs={"rows":1, "cols":40}))
    details = forms.CharField(label='Details', max_length=1000, widget=forms.Textarea(attrs={"rows":5, "cols":40}))
    class Meta:
        model = Question
        fields = ['question', 'details']

#=======
class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField(label='E-mail')
    category = forms.ChoiceField(choices=[('suggestions', 'Suggestions'), ('question', 'Question'), ('report error', 'Report Error'), ('other', 'Other')])
    subject = forms.CharField(required=False)
    body = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.layout = Layout('name', 'email', 'category', 'subject', 'body', Submit('submit','Submit', css_class="button green"))
        #css class portion does not seem to work

# want to be talking to Questions model, dunno if we can go crispy on this one
class QuestionForm(forms.Form):
    question = forms.CharField(max_length=200)
    details = forms.CharField(widget=forms.Textarea, required=False)
    answer = forms.CharField(label='Answer',widget=forms.Textarea(attrs={'placeholder': 'If you learned something, you can submit an answer.'}), required=False, )
    category = forms.CharField()
    #want:    category = forms.ChoiceField(Category.objects.all()) #dunno if this will work
    def __init__(self, *args, **kwargs): #added user param...removed
        super().__init__(*args,**kwargs)
        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.layout = Layout('question','answer','details', 'category', Submit('submit','Submit', css_class="button green"))
