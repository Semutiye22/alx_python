# 8-add_retrieve_users.py

from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///alx_flask_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret_key'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

# Routes for adding and retrieving users
@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        if not name or not email:
            flash("Name and email are required fields.", 'error')
        else:
            existing_user = User.query.filter_by(email=email).first()
            if existing_user:
                flash("Email already taken. Please choose a different email.", 'error')
            else:
                new_user = User(name=name, email=email)
                db.session.add(new_user)
                db.session.commit()
                flash("User added successfully!", 'success')
                return redirect('/users')

    return render_template('add_user.html')

@app.route('/users')
def show_users():
    users = User.query.all()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=5000)