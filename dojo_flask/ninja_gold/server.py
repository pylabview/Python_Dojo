from crypt import methods
from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def process_money():
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)