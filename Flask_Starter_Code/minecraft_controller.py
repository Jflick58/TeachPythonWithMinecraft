from flask import Flask, render_template
from requests import get
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/tree/', methods=['GET'])
def tree():
    return render_template('index.html')

@app.route('/house/', methods=['GET'])
def house():
    return render_template('index.html')

@app.route('/roof/', methods=['GET'])
def roof():
    return render_template('index.html')

@app.route('/custom/', methods=['GET'])
def custom():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False, port=5000)
