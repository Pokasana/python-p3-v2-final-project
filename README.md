# CLI+ORM Application "Artist Finder"

In this README file, you can find explanation of:
* What this app can do
* Structure of files
* What each files for
* How it works  - outline
* How each section actually works

## How this application works
- Users interact with the application through CLI.
- User interaction will trigger objects relational mapping to retrieve the results from the database.

## What user can do with this application
View, edit and delete data of artists and artworks in the database.

---

## The Directory Structure

```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   ├── artist.py
    │   └── art.py
    ├── cli.py
    ├── debug.py
    └── helpers.py
```

This application has two models, artist and art. These files are responsible for the actual interaction, pusing data to/retrieving data from the database.
helpers.py has functions to handle events and works as an intermediate of the database and the user interface.
cli.py contains functions to what and how things are going to be displayed on the comand line interface.

---

## The out like of this app
The user can chose functions by typing in a number or a letter that's listed in the choices.

The menuing is structured with some levels.

─── Main Menu
    └── Artist Management Menu
        ├── Filter Menu
        └── Artist Information Menu
            └── Artwork Information Menu

Each menu has these abilities:
Main Menu
 - To navigate the user to the list of artists
 - Exit from the application

Artist Magement Menu
 - Showing the artist's details
 - To navigate the user to the Filter Menu
 - To add an artist to the database
 - To navigate the user to the previous menu (Main Menu)
 - Exit from the application

Filter Menu
 - To filter the list of artists by location or medium attributes
 - 

User can exit the application from any level.