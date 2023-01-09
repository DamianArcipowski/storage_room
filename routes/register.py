from app import app
from flask import render_template, request, flash
from services.auth_controllers import *
from werkzeug.security import generate_password_hash

@app.route('/register', methods=['GET', 'POST'])
def register():
    
    if request.method == 'POST':
        username = request.form['login']
        password = request.form['password']
        confirm_password = request.form['confirm-password']
        email = request.form['email']
        
        if not is_username_in_database(username):
            if password == confirm_password:
                hashed_password = generate_password_hash(password, salt_length=4)
                add_new_user(username, hashed_password, email)
                flash('Registration process has been finished successfully!', 'auth-success')
            else:
                flash("Passwords doesn't match each other!", 'auth-fail')
        else:
            flash('Username already exists in database!', 'auth-fail')
            
    return render_template('register_page.html')