from flask import Flask
from flask_mongoengine import MongoEngine
from datetime import date

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db': 'your_database',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)

class User(db.Document):
    name = db.StringField(required=True)
    role = db.StringField()
    date_joined = db.DateField()

    def create_user(name, role):
        User(name=name, role=role, date_joined=date.today()).save()
        return

    def retrieve_users():
        return User.objects()

    def update_user(name, role):
        User.objects(name=name).update(role=role)
        return

    def delete_user(name):
        User.objects(name=name).first().delete()
        return