from base import db
import bcrypt

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(32), unique = True)
    password_digest = db.Column(db.String(60))

    def match(self, password):
        return bcrypt.hashpw(password, self.password_digest) == self.password_digest

    def __init__(self, username, password):
        self.username = username 
        self.password_digest = bcrypt.hashpw(password, bcrypt.gensalt(8))

    def __repr__(self):
        return '<id {} username {}>'.format(self.id, self.username)
