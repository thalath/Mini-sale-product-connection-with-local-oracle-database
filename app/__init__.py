from flask import Flask, redirect, url_for
from config import Config
from extensions import db, csrf, login_manager
from app.models.users import User

def create_app(config_class: type[Config] = Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Init extensions
    db.init_app(app)
    csrf.init_app(app)
    login_manager.init_app(app)

    # Flask-Login settings
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Please Sign In to access the System"
    login_manager.login_message_category = "warning"

    @login_manager.user_loader
    def load_user(user_id: str):
        return User.query.get(int(user_id))
    
    # register blueprint
    from app.controller.user_routes import user_bp
    from app.controller.role_routes import role_bp
    from app.controller.permission_routes import permission_bp
    from app.controller.auth_routes import auth_bp
    from app.controller.employee_routes import employee_bp
   
    app.register_blueprint(user_bp)
    app.register_blueprint(role_bp)
    app.register_blueprint(permission_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(employee_bp)

    # 👇 Add this block to "/" goes to the users list
    @app.route("/")
    def home():
        return redirect(url_for('users.index'))

    # Create tables
    with app.app_context():
        from app.models.users import User # noqa F401
        from app.models.roles import Role
        from app.models.permissions import Permission
        db.create_all()

    return app