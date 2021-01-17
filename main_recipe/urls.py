from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.flatpages import views


urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('category/', CategoryView.as_view(), name='category'),
    path('constructor/', ConstructorView.as_view(), name='constructor'),
]


urlpatterns += [
    path('about/', views.flatpage, {'url': '/about/'}, name='about'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
