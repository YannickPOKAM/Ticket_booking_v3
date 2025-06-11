from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, db
from app.utils.auth import generate_token

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/inscription', methods=['GET', 'POST'])
def inscription():
    if request.method != 'POST':
        return render_template('inscription.html')

    email = request.form['email']
    password = request.form['password']
    hashed_password = generate_password_hash(password)

    if user := User.query.filter_by(email=email).first():
        flash("L'utilisateur existe déjà.")
        return redirect(url_for('auth.inscription'))

    new_user = User(email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    flash("Inscription réussie.")
    return redirect(url_for('auth.connexion'))

@auth_bp.route('/connexion', methods=['GET', 'POST'])
def connexion():
    if request.method != 'POST':
        return render_template('connexion.html')

    email = request.form['email']
    password = request.form['password']

    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        flash("Identifiants invalides.")
        return redirect(url_for('auth.connexion'))

    token = generate_token(user.id)
    flash("Connexion réussie.")
    return redirect(url_for('main.index'))  # ou tableau de bord utilisateur

