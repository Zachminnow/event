from django.shortcuts import render
from events.models import EventModel, EventBook
from django.contrib import messages
from .forms import EventForm, EventBookForm
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count


# Create your views here.
def dashboard(request):
    total_events = EventModel.objects.count()
    total_bookings = EventBook.objects.count()

    top_events = (
        EventModel.objects.annotate(num_bookings=Count('bookings'))
        .order_by('-num_bookings')[:5]
    )
    recent_bookings = EventBook.objects.select_related('event').order_by('-id')[:5]

    context = {
        'total_events': total_events,
        'total_bookings': total_bookings,
        'top_events': top_events,
        'recent_bookings': recent_bookings,
    }
    return render(request, 'events/dashboard.html', context)


def event_list(request):
    """
    Display a list of all events
    """
    events = EventModel.objects.all()
    context = {
        'events': events,
    }
    return render(request, 'events/event_list.html', context)


def event_detail(request, event_id):
    event = get_object_or_404(EventModel, pk=event_id)

    bookings = EventBook.objects.filter(event=event)

    # Count bookings by ticket category
    ticket_counts = {
        'VVIP': bookings.filter(ticket_category='VVIP').count(),
        'VIP': bookings.filter(ticket_category='VIP').count(),
        'REGULAR': bookings.filter(ticket_category='REGULAR').count(),
    }

    context = {
        'event': event,
        'bookings': bookings,
        'ticket_counts': ticket_counts,
        'total_bookings': bookings.count(),
    }

    return render(request, 'events/event_detail.html', context)


def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            messages.success(request, f"Event '{event.title}' has been created successfully!")
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventForm()

    return render(request, 'events/create_event.html', {'form': form})


def update_event(request, event_id):
    event = get_object_or_404(EventModel, pk=event_id)

    if request.method == "POST":
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Event '{event.title}' has been updated successfully!")
            return redirect('event_detail', event_id=event.id)
    else:
        form = EventForm(instance=event)
    return render(request, 'events/update_event.html',
                  {'form': form, 'event': event})


def delete_event(request, event_id):
    event = get_object_or_404(EventModel, pk=event_id)

    if request.method == "POST":
        event_name = event.title
        event.delete()
        messages.warning(request, f"Event '{event_name}' has been deleted.")
        return redirect('home')

    return render(request, 'events/delete_event.html', {'event': event})


def book_event(request, event_id):
    event = get_object_or_404(EventModel, id=event_id)

    form = EventBookForm()
    if request.method == 'POST':
        form = EventBookForm(request.POST)
        if form.is_valid():
            # Create booking but don't save to db yet
            booking = form.save(commit=False)
            # Set the event relation
            booking.event = event
            #  Now save to db
            booking.save()

            # Add success message
            messages.success(request, f'You have successfully booked a spot for "{event.title}"!')
            return redirect('booking_success', event_id=event.id)

    else:
        form = EventBookForm()
    context = {
        'form': form,
        'event': event,
    }
    return render(request, 'events/book_event.html', context)


def booking_success(request, event_id):
    return render(request, 'events/booking_success.html')


def booking_list(request):
    bookings = EventBook.objects.all().select_related('event')
    return render(request, 'events/booking_list.html', {'bookings': bookings})


def booking_detail(request, booking_id):
    booking = get_object_or_404(EventBook, id=booking_id)

    return render(request, 'events/booking_detail.html', {'booking': booking})


def update_booking(request, booking_id):
    booking = get_object_or_404(EventBook, pk=booking_id)

    if request.method == "POST":
        form = EventBookForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, f"You updated your booking for {booking.event.title}!")
            return redirect('booking_success', event_id=booking.event.id)
    else:
        form = EventBookForm(instance=booking)

    return render(request, 'events/update_booking.html', {'form': form, 'booking': booking})


def delete_booking(request, booking_id):
    booking = get_object_or_404(EventBook, id=booking_id)
    event_title = booking.event.title

    if request.method == 'POST':
        booking.delete()
        messages.success(request,
                         f'Booking for "{event_title}" has been deleted.')
        return redirect('booking_list')

    context = {
        'booking': booking,
    }
    return render(request, 'events/delete_booking.html', context)
