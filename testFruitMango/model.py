"""Models for mangos app."""

from flask_sqlalchemy import SQLAlchemy

PG_URL = "postgresql:///mangos"
db = SQLAlchemy()


def connect_to_db(app):
    """Connect Flask to PostgreSQL."""

    app.config.update({
        'SQLALCHEMY_DATABASE_URI': PG_URL,
        'SQLALCHEMY_TRACK_MODIFICATIONS': True,
    })
    db.app = app
    db.init_app(app)

class Fruit(db.Model):
    """Fruits."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class Mango(db.Model):
    """Mango."""


class Mango(object):
    """Mango."""

    def __init__(self, melon_type):
        """Initialize mango.

        melon_type: type of melon being built.
        """

        self.fruit_id = fruit_id
        self.mango_country = country
        self.total_cost = total_cost
        self.quantity = quantity
        self.price = price
        self.imgurl = imgurl
        self.commodity = commodity
        self.country = country
        self.f_overhead = fixed_overhead
        self.v_overhead = variable_overhead

    def price_str(self):
        return "$%.2f"%self.price

    def __repr__(self):
        return "<Mango: %s, %s, %s>"%(self.country, self.commodity, self.price_str())

    # def __str__(self):
    #     """Pricing information about mangos."""

    #     # if self.country <= 0:
    #     #     return self.fruit_id 
    #     else:
    #         return "{} {:.2f} tons {}".format(self.country,
    #                                          self.quantity,
    #                                          self.fruit_id,
    #                                          self.f_overhead,
    #                                          self.v_overhead)


