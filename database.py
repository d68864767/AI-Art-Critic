```python
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

class Database:
    def __init__(self, app):
        self.app = app
        db.init_app(app)
        Migrate(app, db)

    class User(db.Model):
        __tablename__ = 'users'

        username = db.Column(db.String(64), primary_key=True, unique=True, nullable=False)
        email = db.Column(db.String(120), unique=True, nullable=False)
        artworks = db.relationship('Artwork', backref='artist', lazy=True)

    class Artwork(db.Model):
        __tablename__ = 'artworks'

        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(120), nullable=False)
        image_path = db.Column(db.String(120), nullable=False)
        critique = db.Column(db.Text, nullable=True)
        artist_username = db.Column(db.String(64), db.ForeignKey('users.username'), nullable=False)

    def get_user(self, username):
        user = self.User.query.filter_by(username=username).first()
        if user:
            return {'username': user.username, 'email': user.email}
        else:
            return None

    def create_user(self, user_data):
        new_user = self.User(username=user_data['username'], email=user_data['email'])
        db.session.add(new_user)
        db.session.commit()

    def update_user(self, username, user_data):
        user = self.User.query.filter_by(username=username).first()
        if user:
            user.email = user_data['email']
            db.session.commit()

    def delete_user(self, username):
        user = self.User.query.filter_by(username=username).first()
        if user:
            db.session.delete(user)
            db.session.commit()
```
