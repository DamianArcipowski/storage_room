from app import app
from flask import render_template

@app.route('/issuing', methods=['GET', 'POST'])
def issuing():
    return render_template('issuing_goods_page.html')