from app import app
from flask import render_template, jsonify
import json
from gdastudio import SQLServer, SQLConnectionPG

@app.route('/overview', methods=['GET', 'POST'])
def overview():
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