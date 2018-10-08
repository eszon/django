from django.shortcuts import render, redirect
from .models import Person
from .forms import PersonForm


# Create your views here.

def person_list(request):
    persons = Person.objects.all()
    return render(request, 'persons.html', {'persons': persons})
  #  return render(request, 'pessoas.html')

def persons_new(request):
    form = PersonForm(request.POST, request.FILES, None)
    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})