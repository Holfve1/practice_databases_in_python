from lib.post_repo import PostRepository
from lib.post import Post


def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = PostRepository(db_connection)
    posts = repository.all()
    assert posts == [
        Post(1, 'My first post', 'This is the content', 7, 1),
        Post(2, 'My second post', 'There is no content', 13, 1),
        Post(3, 'chris post', 'I am the best', 1, 2)

    ]

def test_find_one_record(db_connection):
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = PostRepository(db_connection)
    post = repository.find(1)
    assert post == Post(1, 'My first post', 'This is the content', 7, 1)

def test_if_create_adds_new_user(db_connection):
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = PostRepository(db_connection)
    repository.create(Post(None, 'second post', 'content for two', 7, 2))
    posts = repository.all()
    assert posts == [
        Post(1, 'My first post', 'This is the content', 7, 1),
        Post(2, 'My second post', 'There is no content', 13, 1),
        Post(3, 'chris post', 'I am the best', 1, 2),
        Post(4, 'second post', 'content for two', 7, 2)
    ]

def test_if_record_deleted(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/social_network.sql") # Seed our database with some test data
    repository = PostRepository(db_connection)
    repository.delete(2)
    posts = repository.all()
    assert posts == [
        Post(1, 'My first post', 'This is the content', 7, 1),
        Post(3, 'chris post', 'I am the best', 1, 2)
    ]