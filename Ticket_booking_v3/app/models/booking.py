from app import db

class Booking(db.Model):
    __tablename__ = 'bookings'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    statut = db.Column(db.String(20), default='confirmé')  # ou "annulé"
    date_reservation = db.Column(db.String(100), nullable=False)
