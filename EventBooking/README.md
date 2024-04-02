# Overview
This was a very fun project for me! It is a mock up of an event booking software that allows users to create and RSVP to events. I had never used Django before, and I enjoyed utilizing Python in a web context. Starting the test server requires running the command python3 manage.py runserver, then visiting 127.0.0.1:8000.

I wrote this to give me more experience with web apps, especially those written in Python. I thoroughly enjoyed it!

{Provide a link to your YouTube demonstration.  It should be a 4-5 minute demo of the software running (starting the server and navigating through the web pages) and a walkthrough of the code.}

[Software Demo Video](https://www.loom.com/share/27393c5023d74e7b8b844ee4d79ba5aa?sid=d57c5e00-4eda-4d3f-a55a-420addfc0542)

# Web Pages
## MAIN PAGE
The main page is where users can see all the events that have been added. It is the primary page of the application, and can be accessed from the header as well. The list of events is generated dynamically.

## ADD EVENT PAGE
This page allows users to add an event. It is accessible from the header, and that is how it links to the main page. The form to create the event is dynamically generated in Django.

# Development Environment
This program was developed in VSCode running on a local server. It is written purely in Djano Python, with some CSS.

# Useful Websites
* [Django Official Tutorial (parts 1-6 especially)](https://docs.djangoproject.com/en/5.0/intro/tutorial01/) - EXTREMELY useful in starting your first Django app, covering all aspects from the admin config to the specific views
* [Django Docs - ListView (for homepage)](https://docs.djangoproject.com/en/5.0/ref/class-based-views/generic-display/#listview) - Helped in creating the List and Form views that weren't covered in the official tutorial

# Future Work

* Adding user profiles would be fun to add in the future! Authentication is always a fun problem to solve
* With users, creating a more robust RSVP system would also be a fun feature to add. Showing a guest list  with the names of the attendees and even a way to message them would be interesting
* A screen showing which events your user has RSVPed too would be a beneficial addition as well