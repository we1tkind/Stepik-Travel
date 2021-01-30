from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/departures/<int:departure_id>/')
def render_departures(departure_id):
    return render_template('departure.html')


@app.route('/tours/<int:tour_id>/')
def render_tours(tour_id):
    return render_template('tour.html')


if __name__ == '__main__':
    app.run()
