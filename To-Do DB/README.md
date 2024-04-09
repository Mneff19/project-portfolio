# Overview
To-Do DB is a showcase of how Google Firebase's Firestore can be integrated with a Python script. It is a simple CLI program that runs directly from the main.py script, allowing the user to add, edit, delete, and update entries via the different options in the program.

I wrote this program to build a basic interface with a cloud database, and to work a little with a NoSQL database. It also provided an opportunity to iterate upon and improve some of the code-level practices in [Recipe DB](https://github.com/Mneff19/project-portfolio/tree/main/RecipeDB).

[Software Demo Video - Interface Walkthrough](https://www.loom.com/share/8f76ac265b834ab7a45287d55fbd21bb?sid=f5609955-be2d-4282-8c95-1c08c61eb6ac)
[Software Demo Video - Code Explanation](https://www.loom.com/share/a842e711a08745f1b32a8a742c8eb9e8?sid=bd049c0d-c4e4-45fc-9a73-2f615bfd50a1)

# Cloud Database
The cloud database is Firestore, the solution provided by Google's Firebase. The database is orgranized under one primary collection, then sub-organized by user IDs. Each user ID then has a collection containing all of their personal to-do items. This structure is unique to NoSQL databases and was interesting to research and implement.

# Development Environment
This was developed in Firestore for the initial database setup, with the Python interface being created in VSCode. It utilizes Google's official firebase-admin Python package.

# Useful Websites
- [Google Firebase Docs - Starting a Python Project](https://firebase.google.com/docs/admin/setup?authuser=1#python_1) - Excellent tutorial on starting your Firebase project in Python
- [Google Cloud Docs - Creating a Service Account Key](https://cloud.google.com/iam/docs/keys-create-delete#iam-service-account-keys-create-console) - This was essential in understanding how to connect Python to Google Firebase successfully

# Future Work
- Adding a GUI to this experience would be very fun and would be more intuitive for the user as well, allowing them to simply press an edit icon and adjust the name in line as opposed to working through the menu system.
- Items would be more versatile and powerful if a due date was attached to them, perhaps optionally to not constrict the user to adding a date to it
- I would be interested in leveraging the user's email stored on account creation to send users notifications of each item as the due date approaches