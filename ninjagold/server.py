import random
import time

from flask import Flask, flash, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    session['total'] = 0
    session['log'] = ""
    return render_template('index.html', total=session['total'], log = session['log'])

@app.route('/process_money', methods=['POST'])
def money():
    if 'log' not in session:
        session['log'] = ""
    if request.form['building'] == 'farm':
        farmNum = random.randint(10,20)
        session['total'] += farmNum
        session['log'] = "\n you've earned " + str(farmNum) + " from the farm" + time.strftime('%a %H:%M:%S') + session['log']
        return render_template('index.html')
    elif request.form['building'] == 'cave':
        caveNum = random.randint(5,11)
        session['total'] += caveNum
        session['log'] = "\n you've earned " + str(caveNum) + " from the cave " + time.strftime('%a %H:%M:%S') + session['log']
        return render_template('index.html')
    elif request.form['building'] == 'house':
        houseNum = random.randint(2,6)
        session['total'] += houseNum
        session['log'] = "\n you've earned " + str(houseNum) + " from the house " + time.strftime('%a %H:%M:%S') + session['log']
        return render_template('index.html')
    elif request.form['building'] == 'casino':
        casinoNum = random.randint(-50,51)
        session['total'] += casinoNum
        if casinoNum < 0:
            session['log'] = "\n you've lost " + str(casinoNum) + " ouch! better luck next time " + time.strftime('%a %H:%M:%S') + session['log']
        else:
            session['log'] = "\n you've earned " + str(casinoNum) + " from the casino " + time.strftime('%a %H:%M:%S') + session['log']
        return render_template('index.html')

@app.route('/reset', methods=['post'])
def reset():
    session['total'] = 0
    session['log'] = ""
    return redirect('/')

app.run(debug=True)
