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

book = Book("book", "author", "123")



student = Student("stud1", "stud", book)
if student.role_type == "student":
    print(student.show_book_info())

admin = Admin("abc", "admin", book)


if student.role_type == "student":
    print(student.show_book_info())

new_book = Admin("abcd", "admin", book)

if student.role_type == "student":
    print(student.show_book_info())
new_book_info = admin.add_book("book1", "author2", "987654321")
print(new_book_info)
