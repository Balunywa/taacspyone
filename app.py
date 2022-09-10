from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>This is the default page!</h1>'

@app.route('/twomsprod')
def info():
    return '<h1>This is a PROD ACA Environment!</h1>'

if __name__ == '__main__':
    app.run()
