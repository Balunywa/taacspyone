
from flask import Flask

app = Flask(__name__)



@app.route('/')
def index():
    return '<h1>This is the default page!</h1>'


@app.route('/onemsdev')
def info():
    return '<h1>This is the DEV AKS Environment!</h1>'


if __name__ == '__main__':
    app.run()
    