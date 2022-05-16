from django.shortcuts import render
from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

# Create your views here.


schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    url(r'^$', schema_view)
]