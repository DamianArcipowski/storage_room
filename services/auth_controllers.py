from gdastudio import SQLConnectionPG, SQLServer
import json

with open('config/sql.json', 'r') as config_file:
    file = json.load(config_file)
    server = SQLServer(file['host'], file['database'], file['user'], file['password'])
    
def is_username_in_database(username):
    conn = SQLConnectionPG(server).conn
    cursor = conn.cursor()
    cursor.execute("""Select login FROM store.users WHERE login = '"""+username+"""'""")
    login = cursor.fetchone()
    conn.close()
    return login

def add_new_user(username, password, email):
    conn = SQLConnectionPG(server).conn
    cursor = conn.cursor()
    cursor.execute("""Insert INTO store.users VALUES ('"""+username+"""', '"""+password+"""', '"""+email+"""')""")
    conn.commit()
    conn.close()
    
def get_user_password(username):
    conn = SQLConnectionPG(server).conn
    cursor = conn.cursor()
    cursor.execute("""Select password FROM store.users WHERE login = '"""+username+"""'""")
    password = cursor.fetchone()
    conn.close()
    return password[0]