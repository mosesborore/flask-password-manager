from . import db, bcrypt
from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property
from datetime import datetime


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(64), nullable=False, unique=True)
    email = db.Column(db.String(250), nullable=False, unique=True)
    _master_password = db.Column(db.String(1000), nullable=False)
    accounts = db.relationship("Accounts", backref='user')

    @hybrid_property
    def password(self):
        return self._master_password

    @password.setter
    def password(self, plaintext):
        self._master_password = bcrypt.generate_password_hash(plaintext)

    def is_correct_password(self, plaintext):
        return bcrypt.check_password_hash(self._master_password, plaintext)


class Accounts(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(1000))
    username = db.Column(db.String(256))
    password = db.Column(db.String(512))
    website = db.Column(db.String(1000))
    notes = db.Column(db.String(2000))
    updated = db.Column(db.DateTime(), default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
