from app import app
from flask import render_template

@app.route('/recipients', methods=['GET', 'POST'])
def recipients():
    return render_template('recipients_list_page.html')