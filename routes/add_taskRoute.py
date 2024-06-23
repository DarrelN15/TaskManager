from flask import Blueprint, render_template, redirect, url_for, request, session
from models import Task
from app import db
from datetime import datetime

add_task_bp = Blueprint('add_task_bp', __name__)

@add_task_bp.route('/add_task', methods=['GET', 'POST'])
def add_task():
    if 'user_id' not in session:
        return redirect(url_for('login_bp.login'))
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d')
        priority = request.form['priority']
        status = 'Incomplete'
        user_id = session['user_id']
        task = Task(title=title, description=description, due_date=due_date, priority=priority, status=status, user_id=user_id)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('dashboard_bp.dashboard'))
    return render_template('add_task.html')
