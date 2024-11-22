# django imports
from django.shortcuts import render
from django.db.models import Q

# local imports
from .models import Event

# Create your views here.
def landing_page(request):
    """View for the landing page of the events app.
    """
    query = request.GET.get('q')

    if query:
        events = Event.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
    else:
        events = Event.objects.all()

    return render(request, "landing_page.html", {"events": events, "query": query})
