from flask import Flask, render_template, abort

from consts import INDEX_TOUR_COUNT
from data import tours, departures
from filters import word_agree_with_number, price_limiter, nights_limiter


app = Flask(__name__)
app.jinja_env.filters['word_agree_with_number'] = word_agree_with_number
app.jinja_env.filters['price_limiter'] = price_limiter
app.jinja_env.filters['nights_limiter'] = nights_limiter


@app.route('/')
def index(tours=tours, departures=departures):
    tours = dict(list(tours.items())[:INDEX_TOUR_COUNT])
    return render_template('index.html', tours=tours, departures=departures)


@app.route('/departures/<departure_tag>/')
def render_departures(departure_tag, tours=tours, departures=departures):
    if departure_tag not in departures.keys():
        abort(404)

    filtered_tours = {k: v for k, v in tours.items()
                      if v['departure'] == departure_tag}
    return render_template(
        'departure.html',
        tours=filtered_tours,
        departures=departures,
        departure_tag=departure_tag,
    )


@app.route('/tours/<int:tour_id>/')
def render_tours(tour_id, tours=tours, departures=departures):
    tour = tours.get(tour_id)
    if not tour:
        abort(404)
    return render_template(
        'tour.html', tour=tour, departures=departures,
    )


@app.errorhandler(404)
def page_not_found(error, departures=departures):
    return render_template('page_not_found.html', departures=departures), 404


if __name__ == '__main__':
    app.run(debug=True)
