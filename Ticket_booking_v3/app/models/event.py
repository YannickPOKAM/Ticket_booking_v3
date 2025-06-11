from app import db

class Event(db.Model):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    titre = db.Column(db.String(200), nullable=False)
    date = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    capacite = db.Column(db.Integer)
    categorie = db.Column(db.String(100))

    bookings = db.relationship('Booking', backref='event', lazy=True)
