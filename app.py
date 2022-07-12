from flask import Flask
from api.User import User
from api.Book import Book

app = Flask(__name__)

def index(role):
    if role == "admin":
        User.create_user("angel","member")
        User.update_user("angel", "admin")
        User.delete_user("angel")

    if role == "editor" or role == "admin":
        users = User.retrieve_users()
        for each in users:
            print(each["name"], each["role"], each["date_joined"])
        
        lastBook = Book.get_count()
        nextId = lastBook["bookId"] + 1
        Book.create_book(nextId, "abc", "def", "hello", "testing", 2020, "A", "")
        Book.update_book(1, "abc", "def", "hello", "testing", 2020, "N", "rachel")
        Book.delete_book(nextId)
    
    books = Book.retrieve_books()
    for each in books:
        print(each["bookId"], each["title"], each["description"], each["genre"], each["author"], each["year_published"], each["status"], each["borrower"])
    Book.borrow_book(2, "N", "charles")
    Book.return_book(2, "A")    
    return

index("editor") # change between admin, editor and member 