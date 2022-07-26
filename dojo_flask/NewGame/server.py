import random
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "This is my secret"


@app.route('/')
def index():
    if 'fighters' not in session:
        session['fighters'] = []
        session['winners'] = []
    print(session['fighters'], "in Index method")
    return render_template('index.html')

@app.route('/create', methods=['POST'])
def create():
    print(request.form)
    fighter = {
        'name': request.form['name'],
        'power': int(request.form['power']),
        'luck': int(request.form['luck']),
        'type': request.form['type']
    }
    if fighter['type'] == "extreme":
        fighter['power'] = fighter['power'] * 2
    temp = session['fighters']
    temp.append(fighter)
    session['fighters'] = temp
    print(session['fighters'], "in Create method")
    return redirect('/')
@app.route('/fight', methods=['POST'])
def fight():
    print(request.form)
    for fighter in session['fighters']:
        if fighter['power'] == int(request.form['player1']):
            player1chance = fighter['luck'] * random.randint(1,5)
            print(player1chance, "Player 1 chance")
        if fighter['power'] == int(request.form['player2']):
            player2chance = fighter['luck'] * random.randint(1,5)
            print(player2chance, "Player 2 Chance")
    if int(request.form['player1']) + player1chance > int(request.form['player2']) + player2chance:
        print("Player 1 wins")
        temp = session['winners']
        temp.append("Player 1 wins!")
        session['winners'] = temp
    elif int(request.form['player2']) + player2chance > int(request.form['player1'])+player1chance:
        print("Player 2 wins")
        temp = session['winners']
        temp.append("Player 2 wins!")
        session['winners'] = temp
    else:
        print('Wow I didnt think our randomness would ever tie')
        temp = session['winners']
        temp.append("PseudoRandomness wins!")
        session['winners'] = temp
    return redirect('/')


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)


