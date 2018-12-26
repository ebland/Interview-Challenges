"""Seed process for mangos app database."""

from model import connect_to_db, db, Mango


def seed_mangos():
    """Seed mangos."""

    MX = Mango(country="Mexico")
    BR = Mango(country="Brazil")
    db.session.add(MX)
    db.session.add(BR)
    db.session.commit()

if __name__ == "__main__":
    from flask import Flask   # make mangos app
    app = Flask(__name__)
    connect_to_db(app)        # connect DB to it

    db.create_all()           # make tables
    seed_mangos()               # seed starter data