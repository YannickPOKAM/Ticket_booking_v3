from flask import Blueprint, render_template
from app.routes.booking_routes import booking_bp

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('accueil.html')
    
@main_bp.route('/accueil')
def accueil():
    return render_template('accueil.html')
    
@main_bp.route('/evenements')
def evenements():
    return render_template('evenements.html')

@main_bp.route('/contact')
def contact():
    return render_template('contact.html')

@main_bp.route('/user_dashboard')
def user_dashboard():
    return render_template('user_dashboard.html')

@main_bp.route('/user_profil')
def user_profil():
    return render_template('user_profil.html')

@main_bp.route('/confirmation')
def confirmation():
    return render_template('confirmation.html')









