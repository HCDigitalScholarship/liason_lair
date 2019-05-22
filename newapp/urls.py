# urls for the app
# corresponds to blog urls in tut
from django.urls import include
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
import newapp.views as views

urlpatterns = [
    path('', views.index, name='index'), #creating a view for index page
]
