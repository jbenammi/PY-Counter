from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "ThisismyKey"

@app.route('/')
def index():
	session['num'] += 1
	return render_template('index.html')

@app.route('/plustwo')
def add_two():
	session['num'] += 1
	return redirect('/')

@app.route('/clear')
def reset():
	session['num'] = 0
	return redirect('/')
app.run(debug=True)