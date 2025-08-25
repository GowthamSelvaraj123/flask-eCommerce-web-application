from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

# Initialize extensions
db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()


# User loader for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    # Import User here to avoid circular import
    from app.models import User
    return User.query.get(int(user_id))


def create_app():
    app = Flask(__name__)

    # Configuration
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommercepro.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    # Import blueprints here to avoid circular imports
    from app.routes.main import main_bp
    from app.routes.admin import admin_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp)

    return app
