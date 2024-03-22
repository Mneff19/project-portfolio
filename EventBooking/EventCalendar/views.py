from django.shortcuts import render
from django.utils import timezone
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from .models import Event
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
 
class EventCreate(CreateView):
    # specify the model for create view
    model = Event
 
    # specify the fields to be displayed
    fields = ['event_name', 'event_date', 'event_desc', 'event_img_url']

class EventListView(ListView):
    model = Event
    queryset = Event.objects.order_by('-event_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context

def rsvp(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.event_guest_count = F("event_guest_count") + 1
    event.save()
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    return HttpResponseRedirect(reverse("events:calendar"))