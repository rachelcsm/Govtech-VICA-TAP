from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'your_database',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)

class Book(db.Document):
    bookId = db.IntField()
    title = db.StringField()
    description = db.StringField()
    genre = db.StringField()
    author = db.StringField()
    year_published = db.IntField()
    status = db.StringField()
    borrower = db.StringField()
    
    def to_json(self):
        return {"bookId": self.bookId,
                "title": self.title,
                "description": self.description,
                "genre": self.genre,
                "author": self.author,
                "year_published": self.year_published,
                "status": self.status,
                "borrower": self.borrower}
    
    def create_book(bookId, title, description, genre, author, year_published, status, borrower):
        Book(bookId=bookId, title=title, description=description, genre=genre, author=author, year_published=year_published, status=status, borrower=borrower).save()
        return
    
    def retrieve_books():
        return Book.objects()

    def update_book(bookId, title, description, genre, author, year_published, status, borrower):
        Book.objects(bookId=bookId).update(title=title, description=description, genre=genre, author=author, year_published=year_published, status=status, borrower=borrower)
        return

    def delete_book(bookId):
        Book.objects(bookId=bookId).first().delete()
        return

    def borrow_book(bookId, status, borrower):
        Book.objects(bookId=bookId).update(status=status, borrower=borrower)
        return

    def return_book(bookId, status):
        Book.objects(bookId=bookId).update(status=status, borrower=None)
        return

    def get_count():
        return Book.objects().all().order_by('-id').limit(1)[0].to_json()
