from lib.book import Book

class BookRepository():

    def __init__(self, connection):
        self.connection = connection
    
    def all(self):
        rows = self.connection.execute('SELECT * from books')
        books = []
        for row in rows:
            item = Book(row["id"], row["title"], row["author_name"])
            books.append(item)
        return books


    def find(self, id):
        rows = self.connection.execute(
            'SELECT * from books WHERE id = %s', [id])
        row = rows[0]
        return Book(row["id"], row["title"], row["author_name"])


    def create(self, book):
        self.connection.execute('INSERT INTO books (title, author_name) VALUES (%s, %s)', [
            book.title, book.author_name])
        return None 
       

    def update(self, title, id):
        self.connection.execute('UPDATE books SET title = %s WHERE id = %s' , [title, id])
        return None
       

    # def delete(student)
    #   # Executes the SQL query:
        # DELETE FROM books WHERE id = 1
        

    # Deletes a single Book object