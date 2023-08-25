import re
class Role:
    def __init__(self, name, role_type):
        self.name = name
        self.role_type = role_type
        
class BookStore:
    def __init__(self, title, author, ISBN, genre, avail_status):
        # super().__init__(title, "BookStore")
        self. title = title
        self.author = author
        self.ISBN = ISBN
        self.genre = genre
        self.avail_status = True
    def __str__(self):
        availability = "Available" if self.avail_status else "Not Available"
        return f"Title: {self.title}\n Author: {self.author}\nISBN: {self.ISBN}\nGenre: {self.genre}\nAvailability: {availability}"
# class BookList(BookStore):
#     def get_available_books(self, bookstore):
#         if isinstance(bookstore, BookStore):
#             if self.role_type == "User":
#                 return {book.title: book.author for book in bookstore.books if book.avail_status}
#             else:
#                 return {}
       
#         else:
#             return{}
        # return super().get_available_books(bookstore)
        
class User(Role):
    def __init__(self, name, email,deposit,borrowed_books):
        super().__init__(email, "User")
        self.name = name
        self.email = email
        self.deposit = deposit
        self.borrowed_books = borrowed_books
        
    def __str__(self):
        deposit_status = "Deposit surety has been added" if self.deposit else "Deposit surety has not been added."
        borrowed_books_list = ", ".join(self.borrowed_books)
        return f"Name of the student: {self.name}\n Email of the student: {self.email}\n Deposit: {deposit_status}\n List of borrowed books: {borrowed_books_list}"


class Admin(Role):
    def __init__(self, admin_name, division, shift, admin_id, book_info):
        super().__init__(admin_name, "Admin")
        self.admin_name = admin_name
        self.division = division
        self.shift = shift
        self.admin_id = admin_id
        self.book_info = book_info
    def __str__(self):
        book_list = "\n".join([f'Bookname: {book} and Author: {author}' for book, author in self.book_info.items()])
        
        return f"Name of admin: {self.admin_name} \n Division of the admin: {self.division} \n Employee-shift: {self.shift} \n Admin ID: {self.admin_id} \n {book_list} "


class BookShelf(Role, BookStore):
    def __init__(self, total_genre, section, capacity):
        super().__init__(total_genre, "BookShelf")
        self.total_genre = total_genre
        self.section = section
        self.capacity = capacity
    def __str__(self):
        total_genre_list = ", ".join(self.total_genre)
        sections = ", ".join(self.section)
        return f"List of genre: {total_genre_list} \n Number of sections: {sections} \n Capacity per shelf: {self.capacity}"

def main():
    admin = None
    book_info = {}
    # role = input("You want to enroll as a - [STUDENT/ADMIN] ?")
    # print(role)
    
    while True:
        role = input("You want to enroll as a - [STUDENT/ADMIN]? ").upper()
        if role in ["STUDENT", "S", "ADMIN", "A"]:
            break
        else:
            print("Invalid role. Please choose STUDENT or ADMIN.")
    

    if role.upper() in ["STUDENT", "S"]: 
        print("Book Info:")
        if admin and admin.book_info:
            print("Book Info added by admin:")
            for book, author in admin.book_info.items():
                print(f"Book: {book_name}, Author: {author_name}")
        else:
            print("No Book Info added by admin.")
        # for book_name, author_name in book_info.items():
        #     print(f"Book: {book_name}, Author: {author_name}")
        name = input("Please enter your name: ")
        while True:
            email = input("Please enter the email-id: ")
            if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                break
            else:
                print("Invalid email format. Please enter a valid email.")
            # if book_info:
            #     print("Admin book-info")
            #     for book_name, author_name in book_info.items():
            #         print(f"Book name:{book_name} and Author_name:{author_name}") 
            # else:
            #     print("There's no book added by admin.")
        
        deposit = input("Have sured your deposit amount?")
        borrowed_books = [book.strip() for book in input("Please enter books that you have borrowed (comma-separated):").split(',')]
        user = User(name, email, deposit, borrowed_books)
        
        print(user)

        title = input("Enter the title of the book: ")
        author = input("Enter the author's name: ")
        ISBN = int(input("Enter the ISBN number: "))
        genre = input("What is genre of the book? ")
        avail_status = input("enter")
        book = BookStore(title, author, ISBN, genre, avail_status)
        print(book)

        # available_books = BookList.get_available_books(book)
        # if available_books:
        #     print("Available books:")
        #     for title, author in available_books.items():
        #         # for title, author in available_books.items():
        #         print(f"Title: {title}, Author: {author}")
        #     else:
        #         print("Books are not available for display.")

    elif role.upper() in ["ADMIN", "A"]:

        # num_books = int(input("How many number of books do you want to add? "))
        num_books = int(input("How many number of books do you want to add? "))
        for _ in range(num_books):
            book_name = input("Enter the book name: ")
            author_name = input("Enter the author name: ")
            book_info[book_name] = author_name
        while True:
        # for _ in range(num_books):

            book_name = input("Enter the book name(or type done if you are finished) ")
            if book_name.lower() == "done":
                break
            author_name = input("Enter the author name: ")
            book_info[book_name] = author_name
            
        admin_name = input("Please enter your name: ")
        division = input("What is your division? ")
        shift = input("In which shift you are working? - MORNING/AFTERNOON ").upper()
        admin_id = int(input('what is your employee-ID? -- [PLEASE ENTER INTEGER VALUE] '))
        admin = Admin(admin_name, division, shift, admin_id, book_info)
        print(admin)

        genres = input("Enter a list of genres (comma-separated): ").split(',')
        sections = input("Enter a list of sections (comma-separated): ").split(',')
        capacity = input("Enter the capacity per shelf: ")
        bookshelf = BookShelf(genres, sections, capacity)
        print(bookshelf)
    
    else:
        print("Invalid role. Please choose STUDENT or ADMIN.")

if __name__ == "__main__":
    main()

#atomic habits - james clear
#think and grow rich = napolian hill
#psychology of money - 
#Harry potter - J.K. Rowling
#Pride and prejudice - Jane austin
