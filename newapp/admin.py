from django.contrib import admin
#from .models import Post
# Register
from newapp.models import *

class CourseAdmin(admin.ModelAdmin):
    search_fields = ['title','instructor']
    list_filter = ['semester','department']

admin.site.register(Course, CourseAdmin)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Tag)
admin.site.register(Subtag)

#admin.site.register(User)
