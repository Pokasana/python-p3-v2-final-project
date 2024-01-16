from models.__init__ import CURSOR, CONN
from models.artist import Artist

class Art:

    all = {}

    def __init__(self, title, price, medium, artist_id, id=None):
        self.title = title
        self.price = price
        self.medium = medium
        self.artist_id = artist_id
        self.id = id
    
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if isinstance(value, str) and len(value):
            self._title = value
        else:
            raise ValueError('Title must be a non-empty string')
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if type(value) is int and 100 <= value <= 100000:
            self._price = value
        else:
            raise ValueError("The price must be between 100 and 100000")
        
    @property
    def medium(self):
        return self._medium
    
    @medium.setter
    def medium(self, value):
        if isinstance(value, str) and len(value):
            self._medium = value
        else:
            raise ValueError('Medium must be a non-empty string')

    @property
    def artist_id(self):
        return self._artist_id
    
    @artist_id.setter
    def artist_id(self, artist_id):
        if type(artist_id) == int and Artist.find_by_id(artist_id):
            self._artist_id = artist_id
        else:
            raise ValueError("Artist id must reference an artist in the database")
            
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS arts(
            id INTEGER PRIMARY KEY,
            title TEXT,
            price INTEGER,
            medium TEXT,
            artist_id INTEGER,
            FOREIGN KEY (artist_id) REFERENCES artists(id)
            )
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS arts;
        """

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO arts (title, price, medium, artist_id)
            VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql,(self.title, self.price, self.medium, self.artist_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, title, price, medium, artist_id):
        art = cls(title, price, medium, artist_id)
        art.save()
        return art        


    def update(self):
        sql = """
            UPDATE arts
            SET title = ?, price = ?, medium = ?, artist_id = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.title, self.price, self.medium, self.artist_id, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM arts
            WHERE id  = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        art = cls.all.get(row[0])
        if art:
            art.title = row[1]
            art.price = row[2]
            art.medium = row[3]
            art.artist_id = row[4]
        else:
            art = cls(row[1], row[2], row[3], row[4])
            art.id = row[0]
            cls.all[art.id] = art
        return art
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM arts
        """

        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM arts
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
        