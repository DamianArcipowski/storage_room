from app import app
from flask import render_template, jsonify, request, flash
import json
from gdastudio import SQLServer, SQLConnectionPG
from services.overview_func import *

@app.route('/overview', methods = ['GET', 'POST'])
def overview():
    
    if request.method == 'POST' and request.form.get('form-sender') == 'insert':
        category = request.form['category']
        size = request.form['size']
        color = request.form['color']
        sku = request.form['sku']
        unit = request.form['unit']
        amount = request.form['amount']
        
        if not is_sku_in_database(sku):
            add_goods_to_database(category, sku, unit, amount, size, color)
            flash('Item has been added successfully!', 'success-ins')
        else:
            flash('This SKU exists in database!', 'fail-ins')
        
    elif request.method == 'POST' and request.form.get('form-sender') == 'update':
        sku = request.form['sku']    
        amount = request.form['amount']    

        if is_sku_in_database(sku):
            update_amount_of_goods(sku, amount)
            flash('Amount of items has been updated successfully!', 'success-upd')
        else:
            flash('This SKU exists in database!', 'fail-upd')
            
    elif request.method == 'POST' and request.form.get('form-sender') == 'delete':
        sku = request.form['sku']    

        if is_sku_in_database(sku):
            delete_good_from_database(sku)
            flash(f'SKU {sku} has been deleted successfully!', 'success-del')
        else:
            flash("This SKU doesn't exist in database!", 'fail-del')
        
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