from flask import Flask, render_template, redirect, flash, session
import jinja2

import fruits


app = Flask(__name__)

# A secret key is needed to use Flask sessioning features

app.secret_key = 'this-should-be-something-unguessable'

# Normally, if you refer to an undefined variable in a Jinja template,
# Jinja silently ignores this. This makes debugging difficult, so we'll
# set an attribute of the Jinja environment that says to make this an
# error.

app.jinja_env.undefined = jinja2.StrictUndefined


@app.route("/")
def index():
    """Return homepage."""

    return render_template("homepage.html")


@app.route("/fruits")
def list_fruit():
    """Return page showing all the fruits offered. """

    fruit = fruits.get_all()
    return render_template("all_fruits.html",
                           fruit_list=fruit_list)


@app.route("/fruits/<fruit_id>")
def show_fruit(fruit_id):
    """Return page showing the details of a given fruit.
    Show all info about a fruit. Also, provide a button to buy the fruit.
    """

    fruit = fruits.get_by_id(fruit_id)
    print fruit
    return render_template("fruit_details.html",
                           display_fruit=fruit)


@app.route("/cart")
def show_cart():
    """Display content of cart."""

    # TODO: Display the contents of the cart.

    # The logic here will be something like:
    #
    # - get the cart dictionary from the session
    # - create a list to hold fruit(only mangos for now) 
    #   objects and a variable to hold the total
    #   cost of the order
    # - loop over the cart dictionary, and for each fruit id:
    #    - get the corresponding fruit object
    #    - compute the total cost for that type of fruit
    #    - add this to the order total
    #    - add quantity(in tons), fixed fee, and variable fee
    #      and total cost as attributes on the fruit object
    #    - add the fruit object to the list created above
    # - pass the total order cost and the list of fruit objects 
    #
    # Make sure your function can also handle the case wherein no cart has
    # been added to the session for quoting purposes

    return render_template("cart.html")


@app.route("/add_to_cart/<fruit_id>")
def add_to_cart(fruit_id):
    """Add a fruit to cart and redirect to a cart page.
    When a fruit is added to the cart, redirect browser to the a cart
    page and display a confirmation message: '{{fruit_id}} successfully added to
    cart'."""

    count = 0
    # if 'cart' not in session:
    #     session['cart'] = {}
    cart = {fruit_id: count}

    session['cart'] = session.get('cart', {})

    if fruit_id not in session['cart']:
        count = count + 1

    # session['cart'] = session['cart'].get(count, count + 1)

    flash('You have successfully added %s tons of %s to your cart' % (count, fruit_id))

    return redirect('/cart')
    # TODO: Finish shopping cart functionality

    # The logic here should be something like:
    #
    # - check if a "cart" exists in the session, and create one (an empty
    #   dictionary keyed to the string "cart") if not
    # - check if the desired fruit id is the cart, and if not, put it in
    # - increment the count for that fruit id by 1
    # - flash a success message
    # - redirect the user to the cart page

    return "Oops! This needs to be implemented in person during next interview!"


@app.route("/login", methods=["GET"])
def show_login():
    """Show login form."""

    return render_template("login.html")


@app.route("/login", methods=["POST"])
def process_login():
    """Log user into site.
    Find the user's login credentials located in the 'request.form'
    dictionary, look up the user, and store them in the session.
    """

    # TODO: Need to implement this!

    # The logic here should be something like:
    #
    # - get trader-provided name and password from request.form
    # - use customers.get_by_email() to retrieve corresponding trader
    #   object (if any)
    # - if a trader with that email was found, check the provided password
    #   against the stored one
    # - if they match, store the trader's email in the session, flash a success
    #   message and redirect the trader to the "/fruits" route
    # - if they don't, flash a failure message and redirect back to "/login"
    # - do the same if a trader with that email doesn't exist

    return "Oops! This needs to be implemented"


@app.route("/checkout")
def checkout():
    """Checkout trader, process payment, and ship fruit."""

    # For now, we'll just provide a warning. Completing this is for future
    # developing with States Title.com.

    flash("Sorry! Checkout will be implemented in a future version.")
    return redirect("/fruits")


if __name__ == "__main__":
    app.run(debug=True)