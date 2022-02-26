""" Imports and views required for events app."""
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import EventForm
from .models import Event


@login_required
def view_events(request):
    """ View to render the events page """
    events = Event.objects.all()
    if not events:
        events = None

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
    """ Add event view """
    if request.method == 'POST':
        # If post method check if event doesn't already exist
        # and then add if it doesn't
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)

            try:
                Event.objects.get(
                    name__iexact=form.cleaned_data.get("name"),
                    date__iexact=form.cleaned_data.get("date"),
                    location__icontains=form.cleaned_data.get(
                        "location").split(',')[0])
                messages.error(request, (
                    'Product already exists in database.'))
                return redirect(reverse('events'))

            except Event.DoesNotExist:
                user = User.objects.get(username=request.user)
                instance.user = user
                instance.save()
                messages.success(request, 'Successfully added event!')
                return redirect(reverse('events'))
        else:
            # If form not valid return error
            messages.error(
                request, (
                    'Failed to add event. '
                    'Please ensure the form is valid.'))
            return redirect(reverse('add_event'))
    else:
        # If not post method render template
        form = EventForm()

    template = 'events/add_event.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_event(request, event_id):
    """ Edit event view"""
    get_event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        # If post method update event
        form = EventForm(request.POST, request.FILES, instance=get_event)
        if form.is_valid():
            form.save()
        else:
            messages.error(request, (
                'Failed to update event. '
                'Please ensure the form is valid.'))
            return redirect(reverse(
                'edit_event', kwargs={'event_id': event_id}))

        messages.success(request, 'Thats updated!')
        return redirect(reverse('events'))

    else:
        # If not post method render template with prefilled form
        form = EventForm(instance=get_event)

    template = 'events/edit_event.html'
    context = {
        'form': form,
        'event': get_event,
    }

    return render(request, template, context)


@login_required
def delete_event(request, event_id):
    """ Delete event functionality """
    del_event = get_object_or_404(Event, pk=event_id)
    del_event.delete()
    messages.success(request, 'Event deleted!')
    return redirect(reverse('events'))
