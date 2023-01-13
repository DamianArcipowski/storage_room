from gdastudio import SQLConnectionPG, SQLServer
import json
from datetime import datetime as dt, timedelta
import hashlib
import smtplib
import ssl
from email.message import EmailMessage

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
        
        message = EmailMessage()
        message['Subject'] = 'Link to reset your password'
        message['From'] = credentials['login']
        message['To'] = receiver
        message.set_content("""Hello, \n
You can find a link to reset your password below:
"""+link+"""
It will be active for 24 hours.
If you didn't request about changing your password, please ignore this message.""")
            
        server.send_message(message)
        
def is_link_to_reset_password_still_active(link_id):
    conn = SQLConnectionPG(server).conn
    cursor = conn.cursor()
    cursor.execute("""SELECT current_timestamp - request_date FROM store.change_password_requests WHERE id = '"""+link_id+"""'""")
    interval = cursor.fetchone()
    conn.close()
    
    if timedelta(hours = 24) > interval[0]:
        return True
    else:
        return False
    
def get_email_which_matches_reset_link_id(link_id):
    conn = SQLConnectionPG(server).conn
    cursor = conn.cursor()
    cursor.execute("""Select email FROM store.change_password_requests WHERE id = '"""+link_id+"""'""")
    email = cursor.fetchone()
    conn.close()
    return email[0]
    
def update_new_password_after_reset(link_id, new_password):
    email = get_email_which_matches_reset_link_id(link_id)
    conn = SQLConnectionPG(server).conn
    cursor = conn.cursor()
    cursor.execute("""Update store.users SET password = '"""+new_password+"""' WHERE email = '"""+email+"""'""")
    conn.commit()
    conn.close()