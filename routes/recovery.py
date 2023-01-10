from app import app
from flask import request, flash, render_template
from services.auth_controllers import *

@app.route('/recovery', methods=['GET', 'POST'])
def pass_recovery():
    
    if request.method == 'POST':
        email = request.form['email']
        
        if is_email_in_database(email):
            generate_temporary_id_to_reset_password(email)
    return render_template('recovery_password_page.html')