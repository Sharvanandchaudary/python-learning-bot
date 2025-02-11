from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class UserProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
