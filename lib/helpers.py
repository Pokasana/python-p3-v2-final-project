# lib/helpers.py
from models.artist import Artist
from models.art import Art

##ARTIST'S FUNCTIONS

def list_artists():
    artists = Artist.get_all()
    print("*** Artists ***")

    for artist in artists:
        print(f'{artist.id} ) {artist.name}')

def display_artist_info(id_):
    artist = Artist.find_by_id(id_)
    print("*** Artist Information ***")
    print(f'Name: {artist.name}\nLocation: {artist.location}\nMedium: {artist.medium}')

def filter_artists(attr, value):
    artists = Artist.filter_by_attribute(attr, value)
    if artists:
        for artist in artists:
            print(f'{artist.id} ) {artist.name}')
    else:
        print("No artists found... :(")

def filter_choice_list(attr):
    choices = Artist.get_list_of(attr)
    return choices

def print_choices(li):
    if li:
        for choice in li:
            print(f"{li.index(choice) + 1}: {choice}")
    else:
        print("No selections found... :(")

def display_art_by_artist(id_):
    artist = Artist.find_by_id(id_)
    arts = artist.arts()
    print(f'*** Artworks by {artist.name} ***')
    if arts:
        for art in arts:
            print(f'{arts.index(art) + 1}) "{art.title}" / {art.medium} / {art.price} USD')
    else:
        print("No artworks found... :(")

def create_artist():
    name = input("Enter the artist's name: ")
    location = input("Enter the artist's location: ")
    medium = input("Enter the artist's medium: ")

    try:
        artist = Artist.create(name, location, medium)
        print(f'New artist created! :)')
        print("")
        display_artist_info(artist.id)
    except Exception as exc:
        print("Error creating artist... :( >>", exc)

def update_artist(id_):
    if artist := Artist.find_by_id(id_):
        try:
            name = input("Hit <ENTER> to keep current name, or type in new name: ")
            artist.name = name if name != "" else artist.name
            location = input("Hit <ENTER> to keep current location, or type in new location: ")
            artist.location = location if location != "" else artist.location
            medium = input("Hit <ENTER> to keep current medium, or type in new medium: ")
            artist.medium = medium if medium != "" else artist.medium

            artist.update()
            print(f"{artist.name}'s information has been updated! :)")

        except Exception as exc:
            print(f'Error updating artist information... :( >> ', exc)

def delete_artist(id_):
    if artist := Artist.find_by_id(id_):
        artist.delete()
        print(f'Artist deleted ! :) >> {artist.name}')
    else:
        print(f'Artist not found... :(') 

##ART'S FUNCTIONS
def index_art_id_converter(artist_id, index):
    artist = Artist.find_by_id(artist_id)
    arts = artist.arts()
    art_id = arts[index].id
    return art_id

def create_art(id_):
    artist_id = id_
    title = input("Enter the title: ")
    medium = input("Enter the medium: ")
    price = int(input("Enter the price: "))
    # artist_id = int(input("Enter the artist's id: "))

    try:
        art = Art.create(title, price, medium, artist_id)
        print(f'New art created! :)')
        print("")
        display_art_info(art.id)
    except Exception as exc:
        print("Error creating art... :( >> ", exc)

def update_art(id_, art_id):

    if art := Art.find_by_id(art_id):
        try:
            title = input("Hit <ENTER> to keep current title, or type in new title: ")
            art.title = title if title != "" else art.title
            medium = input("Hit <ENTER> to keep current medium, or type in new medium: ")
            art.medium = medium if medium != "" else art.medium
            price = input("Hit <ENTER> to keep current price, or type in new price: ")
            art.price = int(price) if price != "" else art.price

            art.update()
            print(f'"{art.title}" has been updated! :)')

        except Exception as exc:
            print(f"Error updating artwork... :( >> ", exc)

def delete_art(art_id):

    if art := Art.find_by_id(art_id):
        art.delete()
        print(f'Artwork deleted! :) {art.title}')
    else:
        print(f'Artwork not found... :(')

def exit_program():
    print("Goodbye!")
    exit()

def display_art_info(art_id):
    art = Art.find_by_id(art_id)
    print("*** Artwork Information ***")
    print(f'"{art.title}" / {art.medium} / {art.price} USD')
