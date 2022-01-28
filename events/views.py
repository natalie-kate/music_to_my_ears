from django.shortcuts import render
from .forms import EventForm
from .models import Event

def view_events(request):
    events = Event.objects.all()
    
    context = {
        'events': events,
        'in_events': True,
    }
    return render(request, 'events/events.html', context)

def add_event(request):
    form = EventForm()
    context = {
        'form': form,
    }
    return render(request, 'events/add_event.html')

def edit_event(request, event_id):
    return render(request, 'events/edit_event.html')

def delete_event(request, event_id):
    return render(request, 'events/delete_event.html')
