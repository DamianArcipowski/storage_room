from app import app
from flask import render_template

@app.route('/suppliers', methods=['GET', 'POST'])
def suppliers():
    return render_template('supplier_orders_page.html')