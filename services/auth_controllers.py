from gdastudio import SQLConnectionPG, SQLServer
import json

with open('config/sql.json', 'r') as config_file:
    file = json.load(config_file)
    server = SQLServer(file['host'], file['database'], file['user'], file['password'])
    
def test():
    conn = SQLConnectionPG(server).conn
    cursor = conn.cursor()
    cursor.execute()
    conn.commit()
    conn.close()