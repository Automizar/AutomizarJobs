# app/models/user.py

from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    middle_name = db.Column(db.String(100), nullable=True)
    last_name = db.Column(db.String(100), nullable=False)
    experiences = db.Column(db.PickleType, nullable=True)  # Storing list of experiences
    educations = db.Column(db.PickleType, nullable=True)  # Storing list of educations
    email = db.Column(db.String(120), unique=True, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'<User {self.first_name} {self.last_name}>'
