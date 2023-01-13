from app import app
from flask import request, flash, render_template
from services.auth_controllers import *
from werkzeug.security import generate_password_hash

@app.route('/reset_password/<id>', methods=['GET', 'POST'])
def pass_reset(id):
    
    if request.method == 'POST':
        new_password = request.form['new-password']
        confirm_password = request.form['confirm-password']
        
        if is_link_to_reset_password_still_active(id):
            if new_password == confirm_password:
                hashed_password = generate_password_hash(new_password, salt_length=4)
                update_new_password_after_reset(id, hashed_password)
                flash('Password has been changed successfully!', 'auth-success')
            else:
                flash("Passwords doesn't match each other! Please, try again.", 'auth-fail')
        else:
            flash('Sorry, but your link has expired.', 'auth-fail')
    
    return render_template('reset_password_page.html')