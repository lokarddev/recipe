from django.urls import path
from .views import *

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('category/', CategoryView.as_view(), name='category'),
    path('constructor/', ConstructorView.as_view(), name='constructor'),
    path('about/', AboutView.as_view(), name='about')
]
