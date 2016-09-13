from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key="hi"
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
# notice how we defined which HTTP methods are allowed by this route
@app.route('/results', methods=['POST'])
def create_user():
   session['name'] = request.form['name']
   session['location'] = request.form['location']
   session['language'] = request.form['language']
   session['comment'] = request.form['comment']
   return redirect("/test")

@app.route('/test')
def test():
    return render_template('results.html')
   # return redirect('/')
app.run(debug=True) # run our server
