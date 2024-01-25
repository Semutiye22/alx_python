from flask import Flask, render_template, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret_key'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

# Add your User table creation here

# ...

# Update a User
@app.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        flash("User not found!", 'error')
        return redirect('/')

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        if not name or not email:
            flash("Name and email are required fields.", 'error')
        else:
            existing_user = User.query.filter_by(email=email).first()
            if existing_user and existing_user.id != user_id:
                flash("Email already taken. Please choose a different email.", 'error')
            else:
                user.name = name
                user.email = email
                db.session.commit()
                flash("User updated successfully!", 'success')
                return redirect('/')

    return render_template('update_user.html', user=user)

# Delete a User
@app.route('/delete_user/<int:user_id>', methods=['GET', 'POST'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if user is None:
        flash("User not found!", 'error')
        return redirect('/')

    if request.method == 'POST':
        db.session.delete(user)
        db.session.commit()
        flash("User deleted successfully!", 'success')
        return redirect('/')

    return render_template('delete_user.html', user=user)

# Include other routes and configurations as needed...

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=5000)