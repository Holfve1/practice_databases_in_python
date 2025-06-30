# {{TABLE NAME}} Model and Repository Classes Design Recipe

_Copy this recipe template to design and implement Model and Repository classes for a database table._

## 1. Design and create the Table

If the table is already created in the database, you can skip this step.

Otherwise, [follow this recipe to design and create the SQL schema for your table](https://journey.makers.tech/pages/single-table-design-recipe-template).

*In this template, we'll use an example table `students`*

```
# EXAMPLE

Table: students

Columns:
id | name | cohort_name
```

## 2. Create Test SQL seeds

Your tests will depend on data stored in PostgreSQL to run.

If seed data is provided (or you already created it), you can skip this step.

```sql
-- EXAMPLE
-- (file: spec/seeds_{table_name}.sql)

-- Write your SQL seed here. 

-- First, you'd need to truncate the table - this is so our table is emptied between each test run,
-- so we can start with a fresh state.
-- (RESTART IDENTITY resets the primary key)

TRUNCATE TABLE students RESTART IDENTITY; -- replace with your own table name.

-- Below this line there should only be `INSERT` statements.
-- Replace these statements with your own seed data.

INSERT INTO students (name, cohort_name) VALUES ('David', 'April 2022');
INSERT INTO students (name, cohort_name) VALUES ('Anna', 'May 2022');
```

Run this SQL file on the database to truncate (empty) the table, and insert the seed data. Be mindful of the fact any existing records in the table will be deleted.

```bash
psql -h 127.0.0.1 music_library < seeds_{album}.sql
```

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python


# Model class
# (in lib/album.py)

class Album:
    # 1.  - __init__
        # arguments - id, title, release_year, artist_id
        # returns - None
        # Side effects - None 
    # 2. __eq__ -  assert that the objects it expects are the objects we made based on the database records.
        # arguments - other
        # returns - None
        # side effects - ensures our object is what it expects based on database records 
    # 3. __repr__ - 
        # arguments - None 
        # returns - formatted string
        # Side effects - None 

class AlbumsRepository:


```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# EXAMPLE
# Table name: album 

# Model class
# (in lib/album.py)

class Album:
    def __init__(self, id, title, release_year, artist_id):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f'Album({self.id}, {self.title}, {self.release_year}, {self.artist.id})'


        # Replace the attributes by your own columns.


# We can set the attributes to default empty values and set them later,
# here's an example:
#
# >>> student = Student()
# >>> student.name = "Will"
# >>> student.cohort_name = "September Devs"
# >>> student.name
# 'Will'
# >>> student.cohort_name
# 'September Devs'

```

## 5. Define the Repository Class interface

Your Repository class will need to implement methods for each "read" or "write" operation you'd like to run against the database.

Using comments, define the method signatures (arguments and return value) and what they do - write up the SQL queries that will be used by each method.

```python
# EXAMPLE
# Table name: albums

# Repository class
# (in lib/album_repository.py)

class AlbumRepository:

    def __init__(self, connection) # - initialises connection to database
        # aguments - connection
        # returns - None 
        # Side effects -  creates database connection
  

    def all(self): # retrieve all artists 
        # arguments - None
        # Returns an array of Student objects.
        # Side effects - None 


    def find(self, id):  # Gets a single record by its ID
        # arguments - id
        # Returns a single album object.
        # side effects - None
        # SELECT id, name, cohort_name FROM students WHERE id = $1;


    def create(self, album)  # Create a new album
        # arguments - album
        # returns - None 
        # Side effect - creates new album in albums table 


    def delete(self, id)
        # arguments - id
        # returns - None 
        # side effect - deletes album from albums table 



## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

class album:

"""
Artist constructs with an id, name and genre
"""

def test_album_constructs():
    album = Album(1, "Doolittle", 1989, 1)
    assert album.id == 1
    assert album.title == "doolittle"
    assert album.release_year == 1989
    assert album.artist_id == 1

"""
We can format artists to strings nicely
"""
def test_albums_format_nicely():
    album = Album(1, "Doolittle", 1989, 1)
    assert str(album) == "album(1, "Doolittle", 1989, 1)

"""
We can compare two identical artists
And have them be equal
"""
def test_albums_are_equal():
    album1 = Album(1, "Doolittle", 1989, 1)
    album2 = Album(1, "Doolittle", 1989, 1)
    assert ablum1 == album2


class AlbumRepository:

"""
When we call ArtistRepository#all
We get a list of Artist objects reflecting the seed data.
"""

def test_get_all_records(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/music_library.sql") # Seed our database with some test data
    repository = AlbumRepository(db_connection) # Create a new ArtistRepository
    repository = AlbumRepository(db_connection)  # Create a new ArtistRepository

    albums = repository.all() # Get all artists

        # Assert on the results
    assert albums == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2),
    ]

"""
When we call ArtistRepository#find
We get a single Artist object reflecting the seed data.
"""

def test_get_single_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = ArtistRepository(db_connection)

    album = repository.find(3)
    assert album == Album(3, 'Waterloo', 1974, 2)



"""
When we call AlbumRepository#create
We get a new record in the database.
"""
def test_create_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)

    repository.create(Album(None, "Ok Computer", 2000, 2))

    result = repository.all()
    assert result == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2),
        Album(13, 'Ok Computer', 2000, 2),
    ]

"""
When we call AlbumRepository#delete
We remove a record from the database.
"""

def test_delete_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repository = AlbumRepository(db_connection)
    repository.delete(3) # Apologies to ABBA fans

    result = repository.all()
    assert result == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2),
        Album(13, 'Ok Computer', 2000, 2),
    ]





## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._