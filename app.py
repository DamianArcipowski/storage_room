from flask import Flask

app = Flask(__name__)

from routes.login import *

if __name__ == '__main__':
    app.run(debug=True, port=5000)