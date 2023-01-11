from gdastudio import SQLConnectionPG, SQLServer
import json
from datetime import datetime as dt
import hashlib
import smtplib
import ssl

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

def is_email_in_database(email):
    conn = SQLConnectionPG(server).conn
    cursor = conn.cursor()
    cursor.execute("""Select email FROM store.users WHERE email = '"""+email+"""'""")
    mail = cursor.fetchone()
    conn.close()
    return mail

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

def generate_temporary_id_to_reset_password_and_send_on_email(email):
    current_time = dt.now()
    time_string = current_time.strftime('%Y%m%d%H%M%S')
    encoded_id = hashlib.md5(time_string.encode())
    id_in_hex = encoded_id.hexdigest()
    
    conn = SQLConnectionPG(server).conn
    cursor = conn.cursor()
    cursor.execute("""Insert INTO store.change_password_requests VALUES ('"""+id_in_hex+"""', '"""+email+"""')""")
    conn.commit()
    conn.close()
    return id_in_hex

def send_email_with_link_to_reset_password(receiver, link):
    with open('config/gmail.json', 'r') as jsonfile:
        credentials = json.load(jsonfile)
    
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
        server.login(credentials['login'], credentials['password'])
        
        message = """\
            Subject: Reset your password
            
            
            Your link to reset password in Storage Room App: """+link+""".
            If you didn't request changing your password, please ignore this message."""
            
        server.sendmail(credentials['login'], receiver, message)