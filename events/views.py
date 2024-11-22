# django imports
from django.shortcuts import render

# local imports
from .models import Event

# Create your views here.
def landing_page(request):
    """View for the landing page of the events app.
    """
    events = Event.objects.all()

    return render(request, "landing_page.html", {"events": events})
