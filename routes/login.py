from app import app
from flask import render_template, request, flash, session, redirect, url_for
from services.auth_controllers import *
from werkzeug.security import check_password_hash

app.config['SECRET_KEY'] = '737467726d636f6e66'

@app.route('/', methods=['GET', 'POST'])
def login():
    session['loggedin'] = False
    
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        
        if is_username_in_database(login):
            if check_password_hash(get_user_password(login), password):
                session['loggedin'] = True
                return redirect(url_for('overview'))
            else:
                flash('Incorrect password! Please, try again.')
        else:
            flash("User doesn't exist in database!")
            
    return render_template('login_page.html')