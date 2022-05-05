from flask import current_app as app

@app.route('/')
def main():
    return '<h1> Hello from Flask 2.0! </h1>'
