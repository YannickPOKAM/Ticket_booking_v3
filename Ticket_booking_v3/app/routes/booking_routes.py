from flask import Blueprint, render_template

booking_bp = Blueprint('booking', __name__)

@booking_bp.route('/reservation')
def reservation():
    return render_template('reservation.html')

@booking_bp.route('/paiement')
def paiement():
    return render_template('paiement.html')
