from app import app
from flask import render_template, jsonify, request, flash
import json
from gdastudio import SQLServer, SQLConnectionPG
from services.overview_func import *

@app.route('/overview', methods=['GET', 'POST'])
def overview():
    
    if request.method == 'POST':
        category = request.form['category']
        size = request.form['size']
        color = request.form['color']
        sku = request.form['sku']
        unit = request.form['unit']
        amount = request.form['amount']
        
        if not is_sku_in_database(sku):
            add_goods_to_database(category, sku, unit, amount, size, color)
            flash('Item has been added successfully!', 'success')
        else:
            flash('This SKU exists in database!', 'fail')
        
    return render_template('overview_page.html')


@app.route('/goods_stock/<categories>', methods=['GET'])
def get_stock(categories):
    
    with open('config/sql.json', 'r') as config_file:
        file = json.load(config_file)
        server = SQLServer(file['host'], file['database'], file['user'], file['password'])

    conn = SQLConnectionPG(server).conn
    cursor = conn.cursor()
    cursor.execute("""Select * FROM store.goods_stock WHERE category IN ("""+categories+""")""")
    stock = cursor.fetchall()
    conn.close()
    
    return jsonify(stock)