# app/models/job.py

from app import db

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    location = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text, nullable=True)
    # Add additional fields as needed

    def __repr__(self):
        return f'<Job {self.title}>'
