from flask import Flask, render_template

from consts import INDEX_TOUR_COUNT
from data import tours, departures
from filters import word_agree_with_number, price_limiter, nights_limiter


app = Flask(__name__)
app.jinja_env.filters['word_agree_with_number'] = word_agree_with_number
app.jinja_env.filters['price_limiter'] = price_limiter
app.jinja_env.filters['nights_limiter'] = nights_limiter


@app.route('/')
def index(tours=tours):
    tours = dict(list(tours.items())[:INDEX_TOUR_COUNT])
    return render_template('index.html', tours=tours, departures=departures)


@app.route('/departures/<departure_tag>/')
def render_departures(departure_tag, tours=tours):
    filtered_tours = {k: v for k, v in tours.items()
                      if v['departure'] == departure_tag}
    return render_template(
        'departure.html',
        tours=filtered_tours,
        departures=departures,
        departure_name=departures[departure_tag],
    )


@app.route('/tours/<int:tour_id>/')
def render_tours(tour_id, tours=tours):
    tour = tours[tour_id]
    return render_template(
        'tour.html', tour=tour, departures=departures,
    )


if __name__ == '__main__':
    app.run(debug=True)
