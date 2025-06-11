from flask import Blueprint, request, jsonify
from app import db
from app.models.event import Event
from app.models.booking import Booking
from app.models.user import User
from app.utils.auth import decode_token

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

def is_admin():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        return None
    try:
        token = auth_header.split(" ")[1]
        data = decode_token(token)
        if data['role'] == 'admin':
            return User.query.get(data['user_id'])
    except:
        return None
    return None

@admin_bp.route('/events', methods=['POST'])
def create_event():
    admin = is_admin()
    if not admin:
        return jsonify({"message": "Accès refusé."}), 403

    data = request.get_json()
    event = Event(
        titre=data.get('titre'),
        date=data.get('date'),
        description=data.get('description'),
        capacite=data.get('capacite'),
        categorie=data.get('categorie')
    )
    db.session.add(event)
    db.session.commit()
    return jsonify({"message": "Événement créé avec succès."}), 201

@admin_bp.route('/events/<int:event_id>', methods=['DELETE'])
def delete_event(event_id):
    admin = is_admin()
    if not admin:
        return jsonify({"message": "Accès refusé."}), 403

    event = Event.query.get(event_id)
    if not event:
        return jsonify({"message": "Événement introuvable."}), 404

    db.session.delete(event)
    db.session.commit()
    return jsonify({"message": "Événement supprimé."}), 200

@admin_bp.route('/bookings', methods=['GET'])
def get_all_bookings():
    admin = is_admin()
    if not admin:
        return jsonify({"message": "Accès refusé."}), 403

    bookings = Booking.query.all()
    data = [
        {
            'id': b.id,
            'user': b.user.nom,
            'event': b.event.titre,
            'date': b.date_reservation,
            'statut': b.statut
        }
        for b in bookings
    ]
    return jsonify(data), 200
