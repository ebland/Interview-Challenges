
"""Flask server mangos app."""
import os
from flask import Flask, render_template, request
from model import Mango, connect_to_db

app = Flask(__name__)

connect_to_db(app)

def connect_to_db(app):
    """Connect Flask to PostgreSQL."""

    app.config.update({
        'SQLALCHEMY_DATABASE_URI': PG_URL,
        'SQLALCHEMY_TRACK_MODIFICATIONS': True,
    })
    db.app = app
    db.init_app(app)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/process', methods=['GET', 'POST'])
def mirror():
    """Respond to form with letter & debug info on request."""

    # request.values is a combination of both the form-data and url-data,
    # so it works for both GET and POST requests

    r = request.values

    return render_template(
        'mirror.html',
        fruit_id=r.get('fruit_id'),
        total_cost=r.get('total_cost'),
        quantity=r.get('quantity'),
        mango_country=r.get('country'),
        price=r.get('price'),
        imgurl=r.get('imgurl'),
        commodity=r.get('commodity'),
        country=r.get('country'),
        f_overhead=r.get('fixed_overhead'),
        v_variable=r.get('variable_overhead'),
        method=request.method,
        data=r,
    )

@app.route("/")
def homepage():
    """Simple greeting."""

    return render_template("home.html")


@app.route("/mangos")
def mangos():
    """Show countries for mangos."""

    mangos = Mango.query.all()
    return render_template("mangos.html",
                           mangos=mangos)


@app.route("/err")
def raise_err():
    """Route that throws error; just for testing."""

    raise Exception("Oh no! An error!")


# if __name__ == "__main__":
#     app.run()   # NOTE: not in debug mode!

if __name__ == '__main__':
    app.run(port=int(os.environ.get('PORT', 5000)),
            host='0.0.0.0')