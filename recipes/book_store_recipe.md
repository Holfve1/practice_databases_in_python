# {{book_store}} Model and Repository Classes Design Recipe


## 1. Design and create the Table

DROP TABLE IF EXISTS books;
DROP SEQUENCE IF EXISTS books_id_seq;

-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS books_id_seq;
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author_name VARCHAR(255)
);

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
psql -h 127.0.0.1 your_database_name < seeds_{table_name}.sql
```

## 3. Define the class names

Usually, the Model class name will be the capitalised table name (single instead of plural). The same name is then suffixed by `Repository` for the Repository class name.

```python

class Book


class BookRepository



```

## 4. Implement the Model class

Define the attributes of your Model class. You can usually map the table columns to the attributes of the class, including primary and foreign keys.

```python
# EXAMPLE
# Table name: students

# Model class
# (in lib/student.py)

class Book:
    def __init__(self, id, title, author_name):
        self.id = id
        self.title = title 
        self.author_name = author_name

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Book({self.id}, {self.title}, {self.author_name}")



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


class StudentRepository():
    def __init__(self connection):
    
    
    def all():
        # Executes the SQL query:
        # SELECT id, title, author_name FROM books;

        # Returns an array of Book objects.

        
    def find(id):
        # Executes the SQL query:
        # SELECT id, title, author_name FROM books; WHERE id = $1;

        # Returns a single Book object.

        # Add more methods below for each operation you'd like to implement.

    # def create(student)
    #   # Executes the SQL query:
        # INSERT INTO (id, title, author_name) VALUES (None, 'Nineteen Eighty-Four', 'George Orwell')

        # Creates a single Book object.

       

    # def update(student)
        # Executes the SQL query:
        # UPDATE books SET title = 'IT', author_name = 'Stephen King' WHERE id = 1

        # Updates a single Book object.

       

    # def delete(student)
    #   # Executes the SQL query:
        # DELETE FROM books WHERE id = 1
        

        # Deletes a single Book object.


```

## 6. Write Test Examples

Write Python code that defines the expected behaviour of the Repository class, following your design from the table written in step 5.

These examples will later be encoded as Pytest tests.

Class Book():

    def test_instance():
        book = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
        assert book == "1, 'Nineteen Eighty-Four', 'George Orwell'"



```python
# EXAMPLES

# 1
# Get all students

repo = StudentRepository()

students = repo.all()

len(students) # =>  2

students[0].id # =>  1
students[0].name # =>  'David'
students[0].cohort_name # =>  'April 2022'

students[1].id # =>  2
students[1].name # =>  'Anna'
students[1].cohort_name # =>  'May 2022'

# 2
# Get a single student

repo = StudentRepository()

student = repo.find(1)

student.id # =>  1
student.name # =>  'David'
student.cohort_name # =>  'April 2022'

# Add more examples for each method
```

Encode this example as a test.


## 7. Test-drive and implement the Repository class behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._