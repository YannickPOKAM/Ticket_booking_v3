from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_talisman import Talisman

db = SQLAlchemy()
jwt = JWTManager()
talisman = Talisman()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db.init_app(app)
    jwt.init_app(app)
    #talisman.init_app(app)

    from app.routes.main_routes import main_bp
    from app.routes.booking_routes import booking_bp
    from app.routes.auth_routes import auth_bp
    #from app.routes.event_routes import event_bp
    from app.routes.user_routes import user_bp
    from app.routes.main_routes import main_bp

    
    app.register_blueprint(main_bp)
    app.register_blueprint(booking_bp)
    app.register_blueprint(auth_bp)
    #app.register_blueprint(event_bp)
    app.register_blueprint(user_bp)
    
    
    return app
