# Flask_Web_App_Boilerplate
Simple Flask based Machine Learning Web App which makes call to model with input from user and displays prediction with probability

Goal of this project is to quickly implement your Machine Learning model in a Web based Application, without spending much time on the setup.

It also has a python virtual environment (venv) please activate it by navigating to project directory and run below command without quotes:
"venv\Scripts\activate"

This project will predict weather the given news headline input from user is Fake or real

Flow of the Boilerplate:

    Web address - "http://127.0.0.1:5000/login"
    Login page -> Home page -> Prediction result page

STEPS:
Open cmd in project directory:

	venv\Scripts\activate

Enter below commands:

	set FLASK_APP=fake_news_detection_app.py
	python -m flask run

Open browser:

	http://127.0.0.1:5000/login
	username = admin, password = admin
	Enter a news headline
