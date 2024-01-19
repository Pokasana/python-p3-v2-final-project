from models.__init__ import CURSOR, CONN

class Artist:

    all = {}

    def __init__(self, name, location, medium, id=None):
        self.name = name
        self.location = location
        self.medium = medium
        self.id = id

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value):
            self._name = value
        else:
            raise ValueError('Name must be a non-empty string')
        
    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, value):
        if isinstance(value, str) and len(value):
            self._location = value
        else:
            raise ValueError('Location must be a non-empty string')

    @property
    def medium(self):
        return self._medium
    
    @medium.setter
    def medium(self, value):
        if isinstance(value, str) and len(value):
            self._medium = value
        else:
            raise ValueError('Medium must be a non-empty string')

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS artists(
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT,
            medium TEXT
            )
        """
        
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS artists;
        """

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO artists (name, location, medium)
            VALUES(?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.location, self.medium))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, location, medium):
        artist = cls(name, location, medium)
        artist.save()
        return artist
    
    def update(self):
        sql = """
            UPDATE artists
            SET name = ?, location = ?, medium = ?
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.name, self.location, self.medium, self.id))
        CONN.commit()
    
    def delete(self):
        sql = """
            DELETE FROM artists
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        artist = cls.all.get(row[0])
        if artist:
            artist.name = row[1]
            artist.location = row[2]
            artist.medium = row[3]

        else:
            artist = cls(row[1], row[2], row[3])
            artist.id = row[0]
            cls.all[artist.id] = artist
        return artist
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM artists
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM artists
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def filter_by_attribute(cls, attr, value):
        sql = f"""
            SELECT *
            FROM artists
            WHERE {attr} = ?
        """

        rows = CURSOR.execute(sql,(value,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @staticmethod
    def get_list_of(attr):
        list = set()

        sql = f"""
            SELECT {attr}
            FROM artists
        """

        columns = CURSOR.execute(sql).fetchall()
        for column in columns:
            list.add(column[0])
        return [item for item in list]
        
    def arts(self):
        from models.art import Art
        sql = """
            SELECT *
            FROM arts
            WHERE artist_id = ?
        """

        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Art.instance_from_db(row) for row in rows]