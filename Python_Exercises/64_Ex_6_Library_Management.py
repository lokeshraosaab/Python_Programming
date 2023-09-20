# Write a Library class with no_of_books and books as two instance variables.
# Write a program to create a library from this Library class and show how you can print all books, 
# add a book and get the number of books using different methods. 
# Show that your program doesnt persist the books after the program is stopped!

class Library:
  def __init__(self):
    self.no_of_Books = 0
    self.books = []
    
  def addBook(self, book):
    self.books.append(book)
    self.no_of_Books = len(self.books)

  def showInfo(self):
    print(f"The library has {self.no_of_Books} books.")
  
  def ShowBooks(self):
    print("The books are: ")
    for book in self.books:
      print(book)


L1 = Library()
L1.addBook("Harry Potter1")
L1.addBook("Harry Potter2")
L1.addBook("Harry Potter3")
L1.addBook("Half Girlfriend")
L1.addBook("Two States")

L1.showInfo()
L1.ShowBooks()
