from flask import Blueprint, request, jsonify
from app import db
from app.models.event import Event
from app.models.booking import Booking
from app.models.user import User
from app.utils.auth import decode_token
from datetime import datetime, timezone

user_bp = Blueprint('user', __name__, url_prefix='/user')

# Middleware pour authentifier via JWT
def get_current_user():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return None
    try:
        token = auth_header.split(" ")[1]
        data = decode_token(token)
        return User.query.get(data['user_id'])
    except:
        return None

@user_bp.route('/events', methods=['GET'])
def get_events():
    events = Event.query.all()
    result = [{
        'id': event.id,
        'titre': event.titre,
        'date': event.date,
        'description': event.description,
        'capacite': event.capacite,
        'categorie': event.categorie
    } for event in events]
    return jsonify(result), 200

@user_bp.route('/book/<int:event_id>', methods=['POST'])
def book_event(event_id):
    user = get_current_user()
    if not user:
        return jsonify({"message": "Token invalide ou manquant."}), 401

    event = Event.query.get(event_id)
    if not event:
        return jsonify({"message": "Événement introuvable."}), 404

    if existing := Booking.query.filter_by(user_id=user.id, event_id=event_id).first():
        return jsonify({"message": "Vous avez déjà réservé cet événement."}), 400

    booking = Booking(
        user_id=user.id,
        event_id=event_id,
        statut='confirmé',
        date_reservation=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M')
    )
    db.session.add(booking)
    db.session.commit()
    return jsonify({"message": "Réservation effectuée avec succès."}), 201

@user_bp.route('/reservations', methods=['GET'])
def get_user_bookings():
    user = get_current_user()
    if not user:
        return jsonify({"message": "Token invalide ou manquant."}), 401

    bookings = Booking.query.filter_by(user_id=user.id).all()
    data = [{
        'id': b.id,
        'event': b.event.titre,
        'date': b.date_reservation,
        'statut': b.statut
    } for b in bookings]
    return jsonify(data), 200
