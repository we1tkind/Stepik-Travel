from flask import Flask, render_template

from filters import word_agree_with_number
from consts import INDEX_TOUR_COUNT
from data import tours, departures


app = Flask(__name__)
app.jinja_env.filters['word_agree_with_number'] = word_agree_with_number


@app.route('/')
def index(tours=tours):
    tours = dict(list(tours.items())[:INDEX_TOUR_COUNT])
    return render_template('index.html', tours=tours, departures=departures)


@app.route('/departures/<int:departure_id>/')
def render_departures(departure_id):
    return render_template('departure.html')


@app.route('/tours/<int:tour_id>/')
def render_tours(tour_id):
    return render_template('tour.html')


if __name__ == '__main__':
    app.run()
