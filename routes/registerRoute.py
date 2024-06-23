from flask import Blueprint, render_template, redirect, url_for, request
from models import User
from app import db

register_bp = Blueprint('register_bp', __name__)

@register_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login_bp.login'))
    return render_template('register.html')
