class Book:
    def __init__(self, title, author, ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN

class Student:
    def __init__(self, name, role_type, book):
        self.name = name
        self.role_type = role_type
        self.book = book
        
    def show_book_info(self):
        return f"Student {self.name} is reading '{self.book.title}' by {self.book.author}"

class Admin:
    def __init__(self, name, role_type, book):
        self.name = name
        self.role_type = role_type
        self.book = book
        
    def add_book(self, title, author, ISBN):
        new_book = Book(title, author, ISBN)
        self.book = new_book
        return f"Admin {self.name} added a new book: '{self.book.title}' by {self.book.author}"


book = Book("Sample Book", "Sample Author", "123456789")

# admin = Admin("Bob", "admin", book)

student = Student("Alice", "student", book)
if student.role_type == "student":
    print(student.show_book_info())

admin = Admin("Bob", "admin", book)


if student.role_type == "student":
    print(student.show_book_info())

new_book = Admin("bob", "admin", book)

if student.role_type == "student":
    print(student.show_book_info())
new_book_info = admin.add_book("New Book", "New Author", "987654321")
print(new_book_info)
