from django.urls import path
from . import views
from .views import EventCreate
from .views import EventListView

app_name = "events"
urlpatterns = [
    path("", EventListView.as_view(), name="calendar"),
    path("create", EventCreate.as_view()),
    path("<int:event_id>/rsvp/", views.rsvp, name="rsvp"),
]