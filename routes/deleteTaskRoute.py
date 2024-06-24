from flask import Blueprint, render_template, redirect, url_for, request
from models import db, Task

deleteTask_bp = Blueprint('deleteTask_bp', __name__)

@deleteTask_bp.route('/deleteTask/<int:task_id>', methods=['GET','POST'])
def deleteTask(task_id):
    task = Task.query.get(task_id)
    if request.method == 'POST':
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for('dashboard_bp.dashboard'))
    return render_template('deleteTask.html', task=task)
