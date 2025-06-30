from lib.bookrepository import BookRepository
from lib.book import Book

def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/book_store.sql") # Seed our database with some test data
    repository = BookRepository(db_connection) # Create a new ArtistRepository
    books = repository.all()
    assert books == [
        Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(3, 'Emma', 'Jane Austen'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton')
    ]


def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/book_store.sql") # Seed our database with some test data
    repository = BookRepository(db_connection) # Create a new ArtistRepository
    books = repository.find(1)
    assert books == Book(1, 'Nineteen Eighty-Four', 'George Orwell')

def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/book_store.sql") # Seed our database with some test data
    repository = BookRepository(db_connection) # Create a new ArtistRepository
    repository.create(Book(None, 'IT', 'Stephen King'))
    books = repository.all()
    assert books == [
        Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(3, 'Emma', 'Jane Austen'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton'),
        Book(6, 'IT', 'Stephen King')
    ]

def test_update_record(db_connection):
    db_connection.seed("seeds/book_store.sql")
    repository = BookRepository(db_connection)
    repository.update('yeah', 3) # Apologies to Taylor Swift fans

    books = repository.all()
    assert books == [
        Book(1, 'Nineteen Eighty-Four', 'George Orwell'),
        Book(2, 'Mrs Dalloway', 'Virginia Woolf'),
        Book(4, 'Dracula', 'Bram Stoker'),
        Book(5, 'The Age of Innocence', 'Edith Wharton'),
        Book(3, 'yeah', 'Jane Austen'),
    ]