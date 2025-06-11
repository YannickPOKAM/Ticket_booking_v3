# app/utils/db.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def get_db_connection():
    return db.session
