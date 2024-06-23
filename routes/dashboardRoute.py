from flask import Blueprint, render_template, redirect, url_for, session
from models import Task

dashboard_bp = Blueprint('dashboard_bp', __name__)

@dashboard_bp.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login_bp.login'))
    user_id = session['user_id']
    tasks = Task.query.filter_by(user_id=user_id).all()
    return render_template('dashboard.html', tasks=tasks)
