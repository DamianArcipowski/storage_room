from app import app
from flask import render_template

@app.route('/account', methods=['GET', 'POST'])
def account():
    return render_template('account_overview_page.html')