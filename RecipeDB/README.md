# Overview
This Python project is a simple command line tool to create, view, and edit recipes like your own recipe book! It utilizes SQLite3 - Python's native database library - to maintain the database of recipes.

The program is run by running the Python script and following the CLI prompts. 

I wrote this as a maiden voyage with SQL in Python. To this point I've only ever used an online sandbox to experiment with SQL queries, and I've never written an interface to manage and maintain a database on my own.

{Provide a link to your YouTube demonstration. It should be a 4-5 minute demo of the software running, a walkthrough of the code, and a view of how created the Relational Database.}

[Software Demo Video](http://youtube.link.goes.here)

# Relational Database
I'm using an SQLite3 database to store the recipes, including a primary key, recipe name, ingredients array, and instructions array. 

This is the table within the database, and it is stored in the local project directory.

# Development Environment
The project was built in VSCode using Python and the SQLite3 library - a base library in Python. Since it is run via the command line, all that is required to test the file is to build the script.

# Useful Websites
- [TutorialPoint SQLite Python Overview](https://www.tutorialspoint.com/sqlite/sqlite_python.htm)
- [TutorialPoint AutoIncrement Docs](https://www.tutorialspoint.com/sqlite/sqlite_using_autoincrement.htm)
- [Checking if Table Exists](https://stackoverflow.com/questions/1601151/how-do-i-check-in-sqlite-whether-a-table-exists)

# Future Work

- To make this a true relational database, adding a second table dedicated to ingredients would be ideal
- Adding the ability to search for a recipe based on name or ingedients would make finding recipes easier and more intuitive
- Craeting a GUI would be a great stretch goal for this project