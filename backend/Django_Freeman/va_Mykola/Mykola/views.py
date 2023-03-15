from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView

from Mykola.forms import RegisterPostForm
from Mykola.models import Users


# example for education
def num_home(requests, page_num):
    if requests.GET:
        print(requests.GET)
    return HttpResponse(f'<h1>Тестова сторінка №{page_num}</h1>')

def home_page(requests):
    return render(requests, 'Mykola/home_page_template.html')


def help_page(requests):
    return render(requests, 'Mykola/help_page_template.html')


# class RegisterUser(DataMixin, CreateView):
#     pass

def register_page(requests):
    pass
    # if requests.method == 'POST':
    #     register_form = RegisterPostForm()
    #     if register_form.is_valid():
    #         try:
    #             # Users.objects.create(**register_form.cleaned_data)
    #             return render(requests, 'Mykola/register_page_template.html', {'form': register_form})


def pageNotFound(requests, exception):
    return HttpResponseNotFound('<h1>Сторінку не знайдено</h1>')