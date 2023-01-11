from app import app
from flask import request, flash, render_template
from services.auth_controllers import *

@app.route('/reset_password/<id>', methods=['GET', 'POST'])
def pass_reset(id):
    return f'Hello, your id: {id}'