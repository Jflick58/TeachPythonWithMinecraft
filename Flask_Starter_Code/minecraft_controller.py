from flask import Flask, render_template
from mcpi.minecraft import Minecraft

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/tree/', methods=['GET'])
def tree():
    return render_template('index.html')

#add house 

#add moat 

#add custom


if __name__ == '__main__':
    app.run(debug=False, port=5000)
