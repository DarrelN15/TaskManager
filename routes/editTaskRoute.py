from flask import Blueprint, render_template, redirect, url_for, request, session
from models import db, Task
from datetime import datetime

editTask_bp = Blueprint('editTask_bp', __name__)

@editTask_bp.route('/editTask/<int:task_id>', methods=['GET', 'POST'])
def editTask(task_id):
    task = Task.query.get(task_id)
    if request.method == 'POST':
        task.title = request.form['title']
        task.description = request.form['description']
        task.due_date = datetime.strptime(request.form['due_date'], '%Y-%m-%d')  
        task.priority = request.form['priority']
        task.status = request.form['status']
        db.session.commit()
        return redirect(url_for('dashboard_bp.dashboard'))
    return render_template('editTask.html', task=task)
        