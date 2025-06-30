from lib.user_repo import UserRepository
from lib.user import User


def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = UserRepository(db_connection)
    books = repository.all()
    assert books == [
        User(1, 'Jeff19', 'jeffbloom@email.com'),
        User(2, 'Chris1', 'chrisd17@email.com')
    ]

def test_find_one_record(db_connection):
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = UserRepository(db_connection)
    book = repository.find(1)
    assert book == User(1, 'Jeff19', 'jeffbloom@email.com')

def test_if_create_adds_new_user(db_connection):
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = UserRepository(db_connection)
    repository.create(User(None, 'Dave', 'dave@email.com'))
    books = repository.all()
    assert books == [
        User(1, 'Jeff19', 'jeffbloom@email.com'),
        User(2, 'Chris1', 'chrisd17@email.com'),
        User(3, 'Dave', 'dave@email.com')
    ]

def test_if_record_deleted(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = UserRepository(db_connection)
    repository.delete(2)
    books = repository.all()
    assert books == [
        User(1, 'Jeff19', 'jeffbloom@email.com')
    ]