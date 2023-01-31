from flask import Flask

app = Flask(__name__)

from routes.login import *
from routes.register import *
from routes.overview import *
from routes.password_recovery import *
from routes.password_reset import *
from routes.recipients import *
from routes.goods_issuing import *
from routes.account_overview import *

if __name__ == '__main__':
    app.run(debug=True, port=5000)