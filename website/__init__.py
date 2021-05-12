from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)

    app.config.from_pyfile("config.py")

    # initialize database
    db.init_app(app)
    bcrypt.init_app(app)
    with app.app_context():
        db.create_all()

    # register views
    from .views import views
    from .auth import auth

    app.register_blueprint(views, prefix="")
    app.register_blueprint(auth, prefix="auth")

    from .models import User

    # configure LoginManager
    # if not logged in, redirect to login page
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        # tells flask how we load a user
        # returns the User object whose id == id
        return User.query.get(int(user_id))

    return app
