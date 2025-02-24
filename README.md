# CLI+ORM Application "Artist Finder"

In this README file, you can find an explanation of:
* What this app can do
* Structure of files
* What is each file for
* How it works  - outline
* How each section works

## How this application works
- Users interact with the application through CLI.
- The user interaction will trigger object-relational mapping to retrieve the results from the database.

## What user can do with this application
View, edit, and delete data of artists and artworks in the database.

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

This application has two models, artist and art. These files are responsible for the actual interaction, pushing data to/retrieving data from the database.
helpers.py has functions to handle events and works as an intermediate of the database and the user interface.
cli.py contains functions for what and how things are going to be displayed on the command line interface.

---

## The functionality
The user can choose functions by typing in a number or a letter that's listed in the choices.

The menuing is structured with some levels.

```

    Main Menu
    └── Artist Management Menu
        ├── Filter Menu
        └── Artist Information Menu
            └── Artwork Information Menu

```

Each menu has these abilities:

Main Menu
 - To navigate the user to the list of artists
 - Exit from the application

Artist Management Menu
 - Showing the artist's details
 - To navigate the user to the Filter Menu
 - To add an artist to the database
 - To navigate the user to the previous menu (Main Menu)
 - Exit from the application

Filter Menu
 - To filter the list of artists by location or medium attributes >> the user will be prompted to the Artist Management Menu with the result
 - To navigate the user to the previous menu (Artist Management Menu)
 - Exit from the application

Artist Information Menu
 - Adding a new artwork by the selected artist
 - Updating the selected artist's information
 - Deleting the selected artist from the database
 - To navigate the user to the previous menu(Artist Management Menu)
 - Exit from the application

Artwork Information Menu
 - Updating the selected artwork
 - Deleting the selected artwork
 - To navigate the user to the previous menu(Artist Information Menu of the artist the selected artwork belongs to)
 - Exit from the application


# For Developers
## Helper Functions - lib/helpers.py
    exit_program - exits the user from the application with the exit() function
    list_artists - prints all the artists in the database 
    filter_artists - prints all the artists have the matching attributes that have passed in as an argument
    filter_choice_list - return a list of existing values of the attributes that the user is filtering with
    print_choices - print the values in the filter choice list
    display_artist_info - prints selected artist's information (Name, location, and medium)
    create_artist - creates an artist instance and saves it in the database
    update_artist - update the selected artist instance and update the database accordingly
    delete_artist - delete the selected artist from the database and clear the instance id
    display_art_by_artist - prints all the artworks that belong to the selected artist
    display_art_info - prints selected artwork's information (Title, medium, and price)
    create_art - creates an artwork instance and saves it into the database
    update_art - updates the selected artwork instance and updates the database accordingly
    delete_art - delete the selected artwork from the database and clear the instance id
    index_art_id_converter - returns the artwork's instance id that was found by the index of the list of artworks by the selected artist

## Models
![Alt text](image.png)

## Functions in Models
### Artist
    Setter/Getter for properties (name, location and medium)

    Class Methods
    - create_table(cls)
        Create table 'artists' if it does not already exist
    - drop_table(cls)
        Delete table 'artists' if it exists
    - create(cls, name, location, medium)
        Create a new artist instance, save it in the table, assign the instance id, and add the instance object into the class instance 'all'.
    - instance_from_db(cls, row)
        Retrieve a row from the table and create an artist object based on the values of columns in the row.
    - get_all(cls)
        Retrieve all rows from the artist's table, and return a list of artist objects that were created from each row.
    - find_by_id(cls, id)
        Get a row that has a matching instance id that was passed in as an argument, and return an artist object that was generated from the row.
    - filter_by_attribute(cls, attr, value)
        Take two arguments, attr and value. Return a list of artist objects that were generated by rows with the matching attribute(attr)'s value with the value argument.

    Instance Methods
    - save(self):
        Insert the instance into the artist table, retrieve the row id from the table, and assign it to the artist instance's id attribute. It also adds the artist object into the dictionary 'all'.
    - update(self)
        Update the row in the artist table.
    -delete(self)
        Delete the row from the artist table and dictionary "all", and clear the instance id by assigning it to None.
    - arts(self)
        Import Art class, retrieve all artworks that have the artist instance's id as a foreign key.

    Static Method
    - get_list_of(cls, attr)
        Return a list of attribute(attr)'s values

### Art
    Setter/Getter for properties (title, price, medium, artist_id)

    Class Methods
    - create_table(cls)
        Create table 'arts' if it does not already exist
    - drop_table(cls)
        Delete table 'arts' if it exists
    - create(cls, title, price, medium, artist_id)
        Create a new art instance, save it in the table, assign the instance id, and add the instance object into the class instance 'all'.
    - instance_from_db(cls, row)
        Retrieve a row from the table and create an art object based on the values of columns in the row.
    - get_all(cls)
        Retrieve all rows from the arts table, and return a list of art objects that were created from each row.
    - find_by_id(cls, id)
        Get a row that has a matching instance id that was passed in as an argument, and return an artist object that was generated from the row.

    Instance Methods
    - save(self):
        Insert the instance into the arts table, retrieve the row id from the table, and assign it to the art instance's id attribute. It also adds the art object into the dictionary 'all'.
    - update(self)
        Update the row in the art table.
    -delete(self)
        Delete the row from the art table and dictionary "all", and clear the instance id by assigning it to None.
