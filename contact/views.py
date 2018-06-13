from django.shortcuts import render, get_object_or_404, redirect
from .models import Person
from .forms import PersonForm


def contact_list(request):
    persons = Person.objects.all().order_by('first_name')
    return render(request, 'contact/contact_list.html', {'persons': persons, 'count': persons.count()})


def contact_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    return render(request, 'contact/contact_detail.html', {'person': person})


def contact_new(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=True)
            person.save()
            return redirect('/')
    else:
        form = PersonForm()
    return render(request, 'contact/contact_edit.html', {'form': form})
