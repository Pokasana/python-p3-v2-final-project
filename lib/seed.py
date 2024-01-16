from models.__init__ import CONN, CURSOR
from models.artist import Artist
from models.art import Art

def seed_database():
    Artist.drop_table()
    Artist.create_table()
    Art.drop_table()
    Art.create_table()

    little_thunder = Artist.create("Little Thunder", "Hong Kong", "Painting")
    brian_clarke = Artist.create("Brian Clarke", "London", "Scalpture")
    nate_ross = Artist.create("Nate Ross", "San Francisco", "Photography")
    jon_cornell = Artist.create("Jon Cornell", "San Francisco", "Painting")

    Art.create("School Bus", 2200, "Painting", 1)
    Art.create("GROCERY SHOPPING", 1880, "Painting", 1)
    Art.create("Vesper", 10000, "Sculpture", 2)
    Art.create("Time Lag Zero", 3000, "Sculpture", 2)
    Art.create("Late Afternoon Stroll", 950, "Photography", 3)
    Art.create("The Produce Market", 1000, "Photography", 3)
    Art.create("Sunset in London", 1200, "Photography", 3)


seed_database()
print("Seeded database")