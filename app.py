from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.Config')
    
    # Ensure the instance folder exists
    os.makedirs(app.instance_path, exist_ok=True)

    db.init_app(app)

    with app.app_context():
        from models import User, Task  # Import models here
        db.create_all()  # Create database tables for our data models
        print("Database tables created")

    from routes.loginRoute import login_bp
    from routes.registerRoute import register_bp
    from routes.dashboardRoute import dashboard_bp
    from routes.addTaskRoute import addTask_bp
    from routes.homeRoute import home_bp  # Import the new home blueprint
    from routes.editTaskRoute import editTask_bp  # Import the edit task blueprint
    from routes.deleteTaskRoute import deleteTask_bp  # Import the delete task blueprint

    app.register_blueprint(login_bp)
    app.register_blueprint(register_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(addTask_bp)
    app.register_blueprint(home_bp)  # Register the new home blueprint
    app.register_blueprint(editTask_bp)  # Register the edit task blueprint
    app.register_blueprint(deleteTask_bp)  # Register the delete task blueprint

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
