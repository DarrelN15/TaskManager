from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task_management.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from models import User, Task

    with app.app_context():
        db.create_all()

    from routes.loginRoute import login_bp
    from routes.registerRoute import register_bp
    from routes.dashboardRoute import dashboard_bp
    from routes.add_taskRoute import add_task_bp

    app.register_blueprint(login_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(add_task_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
