from app import app
from flask import render_template, request, flash
from services.recipients_func import *

@app.route('/recipients', methods=['GET', 'POST'])
def recipients():
    
    if request.method == 'POST' and request.form.get('new-recipient') == 'insert':
        name = request.form['name']
        surname = request.form['surname']
        uid = request.form['uid']
        departament = request.form['departament']
        
        if is_userid_in_database(uid):
            add_new_recipient_to_database(name, surname, uid, departament)
        else:
            flash('')
            
    recipients = get_recipients_from_database()
            
    return render_template('recipients_list_page.html', recipients = recipients)