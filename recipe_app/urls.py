from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.flatpages import views


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('profile/', UserProfile.as_view(), name='user_profile'),
    path('category/', CategoryView.as_view(), name='category'),
    path('constructor/', ConstructorView.as_view(), name='constructor'),
    path('add_recipe/', AddRecipe.as_view(), name='add_recipe'),
    path('filter/', FilterView.as_view(), name='filter'),
    path('search/', SearchView.as_view(), name='search'),
    path('category/<int:pk>/', CategoryList.as_view(), name='category_list'),
    path('recipe_list/', RecipeList.as_view(), name='recipe_list'),
    path('topic_list/', TopicList.as_view(), name='topic_list'),
    path('topic_detail/<int:pk>/', TopicDetail.as_view(), name='topic_detail'),
    path('recipe_detail/<int:pk>/', RecipeDetail.as_view(), name='recipe_detail'),
    path('review/<int:pk>/', AddTopicReview.as_view(), name='topic_review')
]


urlpatterns += [
    path('about/', views.flatpage, {'url': '/about/'}, name='about')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
