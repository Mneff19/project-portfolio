import datetime
from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Event(models.Model):
    event_name = models.CharField("event name", max_length=75, default='Event Name')
    event_date = models.DateTimeField("event date", default=timezone.now)
    event_desc = models.CharField("event description", max_length=300, default='Event description, lorem ipsum dolor sit amet consectetur adipisicing elit.')
    event_img_url = models.URLField("event image url", default='https://picsum.photos/500/300')
    event_guest_count = models.IntegerField("event guest count", default='0')

    def __str__(self):
        return self.event_name
    
    def is_past(self):
        return self.event_date <= timezone.now()
    
    def get_absolute_url(self):
        return "http://127.0.0.1:8000/calendar"