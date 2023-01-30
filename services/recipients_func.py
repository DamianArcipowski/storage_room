from gdastudio import SQLServer, SQLConnectionPG
import json

with open('config/sql.json', 'r') as config_file:
    file = json.load(config_file)
    server = SQLServer(file['host'], file['database'], file['user'], file['password'])

def add_new_recipient_to_database(name, surname, uid, departament):
    conn = SQLConnectionPG(server).conn
    cursor = conn.cursor()
    cursor.execute("""Insert INTO store.recipients VALUES ('"""+name+"""', '"""+surname+"""', '"""+uid+"""', '"""+departament+"""')""")
    conn.commit()
    conn.close()
    
def is_userid_in_database(uid):
    conn = SQLConnectionPG(server).conn
    cursor = conn.cursor()
    cursor.execute("""Select uid FROM store.recipients WHERE uid = '"""+uid+"""'""")
    uid = cursor.fetchone()
    conn.close()
    return uid

def get_recipients_from_database():
    conn = SQLConnectionPG(server).conn
    cursor = conn.cursor()
    cursor.execute("""Select * FROM store.recipients""")
    recipients = cursor.fetchall()
    conn.close()
    return recipients