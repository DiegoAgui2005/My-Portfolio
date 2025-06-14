class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.avaible = False
            print(f"El libro {self.title} ha sido prestado")
        else:
            print(f"El libro {self.title} no está disponible")
            
    def return_book(self):
        self.available = True
        print(f"El libro {self.title} ha sido devuelto")
        
class User:
    def __init__(self,name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []
        
    def borrow_book(self, books):
        if books.available:
            books.borrow()
            self.borrowed_books.append(books)
        else:
            print(f"El libro {books.title} no está disponible")
    def return_book(self,book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"El libro {book.title} no ha sido prestado por {self.name}")
            
class Library:
    def __init__(self):
        self.books = []
        self.users = []
        
    def add_book(self,book):
        self.books.append(book)
        print(f"El libro {book.title} ha sido añadido a la biblioteca")
        
    def register_user(self,user):
        self.users.append(user)
        print(f"El usuario {user.name} ha sido registrado")
    
    def show_books(self):
        print("Libros disponibles:")
        for book in self.books:
            if book.available:
                print(f"{book.title} por {book.author}")
                
#Crear los libros             
book1 = Book("El principito", "Antoine de Saint-Exupéry")
book2 = Book("El señor de los anillos", "J.R.R. Tolkien")
book3 = Book("Cien años de soledad", "Gabriel García Márquez")
book4 = Book("Tron El Legado", "Steven Lisberger")

#Crear los usuarios
user1 = User("Diego", "001")
user2 = User("Juan", "002")

#Crear Biblioteca
library = Library()
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.register_user(user2)
library.register_user(user1)

#Realizar Préstamo
user2.borrow_book(book2)

#Mostrar libros disponibles
library.show_books()

#Devolver libro
user2.return_book(book2)