from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView
from rest_framework import generics

# from va_Mykola.Mykola.models import Users
# from Django_Freeman.va_Mykola.Mykola.serializers import MykolaSerializer
# from Mykola.forms import RegisterPostForm

from .models import *
from .serializers import FeaturesSerializer


class FeaturesAPIView(generics.ListAPIView):
    queryset = Features.objects.all()
    serializer_class = FeaturesSerializer
# example for education


def pageNotFound(requests, exception):
    return HttpResponseNotFound('<h1>Сторінку не знайдено</h1>')



