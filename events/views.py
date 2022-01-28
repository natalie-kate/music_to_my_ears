# Imports and views required for events app.
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import EventForm
from .models import Event


@login_required
def view_events(request):
    # View to render the events page
    events = Event.objects.all()

    if request.GET:
        # Returns any event search results
        if 'search' in request.GET:
            search = request.GET['search']
            searches = Q(name__icontains=search) | Q(
                location__icontains=search) | Q(details__icontains=search)
            events = events.filter(searches)
            if not events:
                # If no results from search, show error message
                # and return user to events page
                messages.error(
                    request, (
                        "Sorry your search didn't match any of our events"))
                return redirect(reverse('events'))

        if not search:
            # If search submitted empty, return error
            # message and return user to events page
            messages.error(
                request, "Oops you need to enter a search keyword first")
            return redirect(reverse('events'))

    context = {
        'events': events,
        'in_events': True,
    }
    return render(request, 'events/events.html', context)


@login_required
def add_event(request):
    form = EventForm()
    context = {
        'form': form,
    }
    return render(request, 'events/add_event.html')


@login_required
def edit_event(request, event_id):
    get_event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=get_event)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, (
                'Failed to update event. '
                'Please ensure the form is valid.'))

        messages.success(request, 'Thats updated!')
        return redirect(reverse('events'))

    else:
        form = EventForm(instance=get_event)

    template = 'events/edit_event.html'
    context = {
        'form': form,
        'event': get_event,
    }

    return render(request, template, context)


@login_required
def delete_event(request, event_id):
    # Delete event functionality
    del_event = get_object_or_404(Event, pk=event_id)
    del_event.delete()
    messages.success(request, 'Event deleted!')
    return redirect(reverse('events'))
