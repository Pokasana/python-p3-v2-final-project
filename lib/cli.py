# lib/cli.py

from helpers import (

    exit_program,
    list_artists,
    filter_artists,
    filter_choice_list,
    print_choices,
    display_artist_info,
    create_artist,
    update_artist,
    delete_artist,
    display_art_by_artist,
    display_art_info,
    create_art,
    update_art,
    delete_art,
    index_art_id_converter
)

def main():
    main_menu()
    while True:
        choice = input("> ")
        if choice.lower() == "v":
            list_artists()
            artists()
        elif choice.lower() == "e":
            exit_program()
        else:
            print("Invalid choice")

def artists():
    artist_menu()
    while True:
        choice = input("> ")
        if choice.lower() == "f":
            artist_filter()
        elif choice.lower() == "a":
            create_artist()
            blank()
            list_artists()
            artists()
        elif choice.lower() == "b":
            main()
        elif choice.lower() == "e":
            exit_program()
        elif type(int(choice)) is int: #Need to verify it is within artist list
            id_ = int(choice)
            blank()
            display_artist_info(id_)
            blank()
            display_art_by_artist(id_)
            blank()
            artist_info(id_)
        else:
            print("Invalid choice")

def artist_info(id_):
    artist_info_menu()
    while True:
        choice = input("> ")
        if choice.lower() == "a":
            create_art(id_)
            blank()
            display_artist_info(id_)
            blank()
            display_art_by_artist(id_)
            blank()
            artist_info(id_)
        elif choice.lower() == "u":
            update_artist(id_)
            blank()
            display_artist_info(id_)
            blank()
            display_art_by_artist(id_)
            blank()
            artist_info(id_)
        elif choice.lower() == "d":
            delete_artist(id_)
            blank()
            list_artists()
            artists()
        elif choice.lower() == "b":
            list_artists()
            artists()
        elif choice == "e" or choice == "E":
            exit_program()
        elif type(int(choice)) is int: #Need to verify it is within art list
            index = int(choice) - 1
            art_id = index_art_id_converter(id_, index)
            display_art_info(art_id)
            art_info(id_, art_id)
        else:
            print("Invalid choice")

def artist_filter():
    artist_filter_menu()
    while True:
        choice = input("> ")
        if choice.lower() == "l" :
            li = filter_choice_list("location")
            print_choices(li)
            
            num = int(input("   Enter the number: "))
            value = li[num - 1]

            blank()
            print(f"*** Artists in {value} ***")
            filter_artists("location", value)
            artists()

        elif choice.lower() == "m":
            li = filter_choice_list("medium")
            print_choices(li)
            
            num = int(input("   Enter the number: "))
            value = li[num - 1]

            blank()
            print(f"*** Artist with {value} ***")
            filter_artists("medium", value)
            artists()
            blank()
        elif choice.lower() == "b":
            main()
        elif choice.lower() == "e":
            exit_program()
        else:
            print("Invalid choice")

def art_info(id_, art_id):
    art_info_menu()
    while True:
        choice = input("> ")
        if choice.lower() == "u":
            update_art(id_, art_id)
            display_art_info(art_id)
            art_info(id_, art_id)

        elif choice.lower() == "d":
            delete_art(art_id)
            blank()
            display_artist_info(id_)
            blank()
            display_art_by_artist(id_)
            blank()

            artist_info(id_)

        elif choice.lower() == "b":
            blank()
            display_artist_info(id_)
            blank()
            display_art_by_artist(id_)
            blank()
            artist_info(id_)
        elif choice.lower() == "e":
            exit_program()
        else:
            print("Invalid choice")


#Format
def blank():
    print("")

#Menu
def main_menu():
    print("")
    print(" =================== ")
    print("    ARTIST FINDER    ")
    print(" =================== ")
    print("Welcome to Artist Finder!")
    print("")
    print("""
        --- MAIN MENU ---
        Please select an option:
          v) VIEW ARTISTS
          e) EXIT THE PROGRAM
    """)

def artist_menu():
    print("""
        --- ARTIST MANAGEMENT MENU ---
        Enter artist's id for information
                    or
        Please select an option:
          f) FILTER ARTISTS
          a) ADD A NEW ARTIST
          b) GO BACK TO MAIN MENU
          e) EXIT THE PROGRAM
    """)

def artist_info_menu():
    print("""
        --- ARTIST INFORMATION MENU ---
        Enter number for artwork's details
                    or
        Please select an option:
          a) ADD A NEW ARTWORK
          u) UPDATE THIS ARTIST
          d) DELETE THIS ARTIST
          b) GO BACK TO THE PREVIOUS MENU
          e) EXIT THE PROGRAM
          """)
    
def artist_filter_menu():
    print("""
        --- FILTER MENU ---
        Filter artist by:
          l) LOCATION
          m) MEDIUM

        Or:
          b) GO BACK TO THE MAIN MENU
          e) EXIT THE PROGRAM
          
        """)

def art_info_menu():
    print("""
        --- ARTWORK INFORMATION MENU ---
        Please select an option:
          u) UPDATE THIS ARTWORK
          d) DELETE THIS ARTWORK
          b) GO BACK TO PREVIOUS MENU
          e) EXIT THE PROGRAM
    """)

if __name__ == "__main__":
    main()
