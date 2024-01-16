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

This application has two models, artist and art.
These files are responsible for the actual interaction witth the database.
helpers.py is to handle events and connect the database to the user interface.
cli.py contains functions to manage the appearance on the comand line interface.


---

## How it works


---

## How each section actually works

