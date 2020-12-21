from django.urls import path
from .views import *

urlpatterns = [
    path('home/', Home.as_view(), name='home'),
    path('category/', Category.as_view(), name='category'),
    path('constructor/', Constructor.as_view(), name='constructor'),
    path('about/', About.as_view(), name='about')
]
