from django.shortcuts import render, get_object_or_404
from .models import Person


def contact_list(request):
    persons = Person.objects.all().order_by('first_name')
    return render(request, 'contact/contact_list.html', {'persons': persons, 'count': persons.count()})


def contact_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, 'contact/contact_detail.html', {'person': person})
