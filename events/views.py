# django imports
from django.shortcuts import render
from django.db.models import Q

# local imports
from .models import Event
from .filters import EventFilter

# Create your views here.
def landing_page(request):
    """View for the landing page of the events app.
    """
    query = request.GET.get('q')

    # Base queryset
    events = Event.objects.all()

    # Apply search if a query exists
    if query:
        events = events.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

    # Apply filtering
    event_filter = EventFilter(request.GET, queryset=events)

    return render(
        request,
        "landing_page.html",
        {
            "events": events,
            "query": query,
            "filter": event_filter,
        }
    )
