from lib.album import Album

class AlbumRepository:

    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute("SELECT * FROM albums")
        albums = []
        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)
        return albums 
    
    def find(self, id):
        rows = self.connection.execute('SELECT * FROM albums WHERE id = %s', [id])
        row = rows[0]  
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])
    
    def create(self, album):
        self.connection.execute("INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)", [album.title, album.release_year, album.artist_id])
        return None 
    
    def delete(self, id):
        self.connection.execute("DELETE FROM albums WHERE id = %s", [id])
        return None