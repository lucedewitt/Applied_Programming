# Library Catalog

The Library Catalog creates a table of books for the user to add to, modify, delete, and search through. Users can find a book, add a book, modify a book's information, delete a book, and look at the stats of the catalog table in the database. The filter option is not yet implemented, but could be coming soon if I choose to continue this project (I wanted to leave it in the outline as a reminder).

## Instructions for Build and Use

Steps to build and/or run the software:

1. Using the VSCode menu, press run
2. If you don't have a run button, run "python library.py" in the terminal

Instructions for using the software:

1. Choose which option on the menu you want to see (0 quits the program)
2. To find a book, enter the title and author using exact spelling and capatlization
3. When updating a book, also use the exact spelling and capatization you want
4. The show stats option is also in a loop, allowing you to leave, or look at the averages/totals/min&max
5. (The other features and menu options are self-explanatory)

## Development Environment

To recreate the development environment, you need the following software and/or libraries with the specified versions:

* Download and install Python from python.org
* Install the Python (microsoft) extention in VSCode
* (Install the newest version of python ideally, but at least version 2.5.x and onwards)
* Press ctrl+shift+P, selection Python: Select Interpreter and choose your Python installation
* If you want to view the database: in VSCode extentions download SQLite Viewer

## Useful Websites to Learn More

I found these websites useful in developing this software:

* SQLite Tutorial (https://www.sqlitetutorial.net/)
* sqlite3 — DB-API 2.0 interface for SQLite databases (https://docs.python.org/3.13/library/sqlite3.html)
* SQLite - Python (https://www.tutorialspoint.com/sqlite/sqlite_python.htm)

## Future Work

The following items I plan to fix, improve, and/or add to this project in the future:

* Add the filter menu option
* Let the user enter genres one at a time (instead of Genre|Genre...)
* Manipulate inputs so books can be found with weirdly inputted capatlization
* Add error handling (non int inputs on menus)