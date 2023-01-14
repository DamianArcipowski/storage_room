from app import app
from flask import render_template

@app.route('/overview', methods=['GET', 'POST'])
def overview():
    return render_template('overview_page.html')