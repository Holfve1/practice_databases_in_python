from lib.book import Book

def test_instance():
    book = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
    assert book.id == 1
    assert book.title == 'Nineteen Eighty-Four'
    assert book.author_name == 'George Orwell'

def test_string_formatted_correctly():
    book = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
    assert str(book) == "Book(1, Nineteen Eighty-Four, George Orwell)" 

def test_compare_2_identical_lists():
    book1 = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
    book2 = Book(1, 'Nineteen Eighty-Four', 'George Orwell')
    assert book1 == book2