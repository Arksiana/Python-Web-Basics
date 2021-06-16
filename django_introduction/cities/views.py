from django.shortcuts import render

from django_introduction.cities.models import Person


def index(req):
    context = {
        'name': 'Doncho',
        'people': Person.objects.all(),
    }
    return render(req, 'index.html', context)
