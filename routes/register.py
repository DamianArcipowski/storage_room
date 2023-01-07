from app import app
from flask import render_template

@app.route('/', methods=['GET', 'POST'])
def register():
    return render_template('registration_page.html')