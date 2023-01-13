from app import app
from flask import request, flash, render_template
from services.auth_controllers import *

@app.route('/recovery', methods=['GET', 'POST'])
def pass_recovery():
    
    if request.method == 'POST':
        email = request.form['email']
        
        if is_email_in_database(email):
            recovery_id = generate_temporary_id_to_reset_password_and_send_on_email(email)
            link_to_reset = f'http://127.0.0.1:5000/reset_password/{recovery_id}'
            send_email_with_link_to_reset_password(email, link_to_reset)
            flash('If passed e-mail exists in our database, we will send you an e-mail with link to reset your password.')
            
    return render_template('recovery_password_page.html')