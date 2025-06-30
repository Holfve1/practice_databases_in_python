from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository
from lib.database_connection import DatabaseConnection

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/music_library.sql")

        self.artist_repository = ArtistRepository(self._connection)
        self.album_repository = AlbumRepository(self._connection)

    def run(self):
        while True:
            print("\nWelcome to the Music Library!")
            print("1. List artists")
            print("2. List albums")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.list_artists()
            elif choice == "2":
                self.list_albums()
            elif choice == "3":
                print("Goodbye!")
                exit()
            else:
                print("Invalid choice, please try again.")

    def list_artists(self):
        artists = self.artist_repository.all()
        print("\nArtists:")
        for artist in artists:
            print(f"{artist.id}: {artist.name}")

    def list_albums(self):
        albums = self.album_repository.all()
        print("\nAlbums:")
        for album in albums:
            print(f"{album.id}: {album.title} by Artist ID {album.artist_id}")


if __name__ == '__main__':
    app = Application()
    app.run()
