from flask import Flask, redirect, render_template, session
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninja():
    displayAll = True
    return render_template('ninjas.html', displayAll=displayAll)

@app.route('/ninjas/<color>')
def getColor(color):
    displayAll = False
    return render_template('ninjas.html', color=color, displayAll=displayAll)

app.run(debug=True)
