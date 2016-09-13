from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
app.counter = 0

def sumSessionCounter():
  try:
    session['counter'] += 1
  except KeyError:
    session['counter'] = 1

@app.route('/')
def index():
    sumSessionCounter()
    return render_template('index.html')

@app.route('/increment', methods=['POST'])
def incrementtwo():
    sumSessionCounter()
    #We only increment by 1 since reloading the page also increments
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    session['counter'] = 0
    return redirect('/')

app.run(debug=True)
