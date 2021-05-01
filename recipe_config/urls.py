from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
# from graphene_django.views import GraphQLView
from recipe_app.api.schema import schema
from graphene_file_upload.django import FileUploadGraphQLView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipe_app.urls')),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('account/', include('allauth.urls')),
    path('graphql', csrf_exempt(FileUploadGraphQLView.as_view(graphiql=True, schema=schema))),
]
