from gdastudio import SQLServer, SQLConnectionPG
import json

with open('config/sql.json', 'r') as config_file:
    file = json.load(config_file)
    server = SQLServer(file['host'], file['database'], file['user'], file['password'])

def add_goods_to_database(category, sku, unit, amount, size = None, color = None):
    conn = SQLConnectionPG(server).conn
    cursor = conn.cursor()
    cursor.execute("""Insert INTO store.goods_stock VALUES ('"""+category+"""', '"""+size+"""', '"""+color+"""',
                   '"""+sku+"""', '"""+unit+"""', '"""+str(amount)+"""')""")
    conn.commit()
    conn.close()
    
def is_sku_in_database(sku):
    conn = SQLConnectionPG(server).conn
    cursor = conn.cursor()
    cursor.execute("""Select * FROM store.goods_stock WHERE sku = '"""+sku+"""'""")
    sku = cursor.fetchone()
    conn.close()
    return sku