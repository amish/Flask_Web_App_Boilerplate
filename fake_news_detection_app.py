from flask import Flask, render_template, redirect, url_for, request
import pickle

app = Flask(__name__)


@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form['username'] != 'admin' or request.form['password'] != 'admin':
			error = 'Invalid Credentials. Please try again.'
		else:
			return redirect(url_for('home'))
	return render_template('login.html', error = error)


@app.route('/home', methods=['GET', 'POST'])
def home(statement = None):
	return render_template('home.html')


@app.route('/result', methods=['GET', 'POST'])
def result(statement = None):
	if request.method == 'POST':
		result, proba = predictValue(request.form['statement'])
		return render_template('result.html', statement = request.form['statement'], final = result, probability = proba)
	return render_template('result.html')


def predictValue(query):
	if query != None:
		model = pickle.load(open('final_model.sav', 'rb'))
		prediction = model.predict([query])
		proba = model.predict_proba([query])
		return prediction, proba