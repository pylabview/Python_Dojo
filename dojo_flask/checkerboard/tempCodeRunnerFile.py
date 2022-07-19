from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           row=8,
                           col=8,
                           color_1="black",
                           color_2="red")
@app.route('/<int:row>')
def row(row):
    return render_template("index.html",
                           row=row,
                           col=8,
                           color_1="black",
                           color_2="red")

@app.route('/<int:row>/<int:col>')
def row_col(row, col):
    return render_template("index.html",
                           row=row,
                           col=col,
                           color_1="black",
                           color_2="red")

@app.route('/<int:row>/<int:col>/<string:one>')
def row_col_one(row, col, one):
    return render_template("index.html",
                           row=row,
                           col=col,
                           color_1=one,
                           color_2="red")
@app.route('/<int:row>/<int:col>/<string:one>/<string:two>')
def row_col_one_two(row, col, one, two):
    return render_template("index.html",
                           row=row,
                           col=col,
                           color_1=one,
                           color_2=two)

if __name__ == "__main__":
    app.run(debug=True)