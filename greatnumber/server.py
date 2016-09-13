import random

from flask import Flask, flash, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def index():
    if "num" not in session:
        session['num']= random.randrange(0,101)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def numSession():

    guess = int(request.form['guess'])
    session['guess'] = guess
    if guess < session['num']:
        flash('Too low', 'error')
    elif guess > session['num']:
        flash('Too high', 'error')
    else:
        flash('Correct, success')
    return render_template('index.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
