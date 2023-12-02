# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

# Import routes after initializing SQLAlchemy
from app.routes import job_routes

# Import models to ensure they are registered with SQLAlchemy
from app import models
