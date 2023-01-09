from app import app

@app.route('/overview', methods=['GET', 'POST'])
def overview():
    return 'Hello main page'