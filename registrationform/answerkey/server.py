from flask import Flask, redirect, request, session, flash, render_template
import re
import datetime

app = Flask(__name__)
app.secret_key = 'very secret'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
PASSWORD = re.compile(r'.*?[A-Z]+.*?[0-9]+|.*?[0-9]+.*?[A-Z]')

@app.route('/')
def new():
    print datetime.date.today()
    return render_template('create.html')

@app.route('/register', methods = ['POST'])
def create():
    print request.form
    data = request.form
    d = datetime.datetime.strptime
    errors = {}
    # d.strftime("%d/%m/%y")
    try:
        d(data['birthday'], "%m/%d/%Y")
        if d(data['birthday'], "%m/%d/%Y") >= datetime.datetime.today():
            errors['birthday'] = "You aren't born yet!"

    except:
        errors['birthday'] = 'Not a valid birthday'


    if len(data['first_name']) < 1:
        errors['first_name'] = 'First name must exist'
    if len(data['last_name']) < 1:
        errors['last_name']= 'Last name must exist'
    if len(data['email']) < 1:
        errors['email']= 'email must exist'

    elif not EMAIL_REGEX.match(rdata['email']):
        errors['email']= 'must be a valid email address'

    if len(data['password']) < 7:
        errors['password']= 'Password must be at least 8 characters'
    elif not PASSWORD.match(data['password']):
        errors['password']='Password must contain at least 1 capital and one number'


    if not data['password'] == data['confirm_password']:
        errors['confirm_password']= 'Password and Password confirmation must match'
    if len(errors) > 0:
        flash(errors)
        return redirect('/')
    return render_template('show.html')

if __name__ == '__main__':
    app.run(debug=True)
