from django.contrib import admin
#from .models import Post
# Register
from newapp.models import *

class CourseAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ['semester']


admin.site.register(Course, CourseAdmin)