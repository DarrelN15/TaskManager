from flask import Blueprint, render_template, redirect, url_for, session, current_app
from models import Task

dashboard_bp = Blueprint('dashboard_bp', __name__)

@dashboard_bp.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login_bp.login'))
    
    user_id = session['user_id']
    current_app.logger.info(f"Fetching tasks for user_id: {user_id}")
    
    tasks = Task.query.filter_by(user_id=user_id).all()
    
    current_app.logger.info(f"Number of tasks fetched: {len(tasks)}")
    
    return render_template('dashboard.html', tasks=tasks)
