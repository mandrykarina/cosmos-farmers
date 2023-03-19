import os
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

import mainapp

app = Flask(__name__)

points = mainapp.get_new_flight_assigment()

class FlightAssign(FlaskForm):
    assign = StringField('Полетное задание', validators=[DataRequired()])
    submit = SubmitField('Рассчитать')

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
