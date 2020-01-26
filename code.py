from flask import Flask, render_template
from data import title, subtitle, description, departures, tours


app = Flask('fla')

@app.route('/')
def index():
    return render_template('index.html', tours=tours, title=title, subtitle=subtitle, description=description)

@app.route('/from/<direction>/')
def from_direction(direction):
    return render_template('direction.html', direction=direction, departures=departures, tours=tours)

@app.route('/tours/<int:id>/')
def tour_page(id):
    return render_template('tour.html', tour=tours[id], departures=departures)


app.run(debug=True)