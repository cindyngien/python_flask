from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key="hi"
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")
# notice how we defined which HTTP methods are allowed by this route
@app.route('/process', methods=['post'])
def process():


    if len(request.form['name']) < 1:
        flash("Name cannot be empty!")
        return redirect('/')
    if  len(request.form['comment']) < 1:
        flash("Comment cannot be empty!")
        return redirect('/')
    if  len(request.form['comment']) > 255:
        flash("Why would you write so much?")
        return redirect('/')

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
