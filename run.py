# run.py

from app import app

if __name__ == '__main__':
    from app import db
    db.create_all()  # Create database tables for our data models
    app.run(debug=True)
