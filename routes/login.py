from app import app
from flask import render_template, request, flash, session

app.config['SECRET_KEY'] = '737467726d636f6e66'

@app.route('/', methods=['GET', 'POST'])
def login():
    session['loggedin'] = False
    
    if request.method == 'POST':
        flash('Incorrect login or password!')
    return render_template('login_page.html')