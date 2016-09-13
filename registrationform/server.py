# import Flask
from flask import Flask, render_template, redirect, request, session, flash
# the "re" module will let us perform some regular expression operations
import re
# create a regular expression object that we can use run operations on
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
@app.route('/', methods=['GET'])
def index():
  return render_template("index.html")

@app.route('/process', methods=['POST'])
def submit():
    session['first_name'] = request.form['first_name']
    session['last_name'] = request.form['last_name']
    session['emailaddress'] = request.form['emailaddress']
    session['password'] = request.form['password']
    session['confirmpassword'] = request.form['confirmpassword']

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    emailaddress = request.form['emailaddress']
    password = request.form['password']
    confirmpassword = request.form['confirmpassword']

        #email Address
    if emailaddress == '':
        flash("Email cannot be blank", 'error')
    elif not EMAIL_REGEX.match(emailaddress):
        flash("Invalid Email Address!", 'error')

    #first_name
    if first_name == '':
        flash("First name cannot be blank", 'error')
    elif not first_name.isalpha():
        flash("First name cannot contain any numbers", 'error')
    #last_name
    if last_name == '':
        flash("Last Name cannot be blank", 'error')
    elif not last_name.isalpha():
        flash("Last name cannot contain any numbers", 'error')

    #password
    if password == '':
        flash("Password cannot be empty", 'error')
    elif len(password) < 8:
        flash("Password has to be greater than 8 characters", 'error')

    #confirmpassword
    if confirmpassword == '':
        flash("Please confirm your password", 'error')
    elif confirmpassword != password:
        flash("Please match your password", 'error')
    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

app.run(debug=True)
