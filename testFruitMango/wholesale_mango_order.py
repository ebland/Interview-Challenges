from mangos import Mangos
import sys

def show_help():
    print """
wholesale_mango_order.py
  Master Control Program for Automated Mango Order Fullfillment

This program processes order from an order log file and controls the purchasing 
of mangos providing live pricing for the fruit by the ton in the countries 
they are available to purchase from.

Usage:

    python wholesale_mango_order.py [logfile]

Where:

  [logfile]
    3rd-party log file you would like to process.


The cost is computed from a combination of the your input along with 
current market overhead data (fees and taxes) that we are getting from a 3rd-party API.

● The cost per pound is calculated as the price from the trader + the “variable overhead”
  from our data vendor.

● The cost per trade is strictly the “fixed overhead” from our data vendor.
  3rd-Party Data We have a deal with a 3rd-party that provides us the latest
  fixed and variable overhead data for various fruits across a variety of countries.

The data is provided to us on a nightly basis as a flat file transmitted via FTP.
"""

def get_fruit_price_by_country(mangos):
    list_fruit=[]
    # """Given fruit name, return the price of mangos.

    # Here are a list of countries and prices: (flat file 3rd party)
    # MX 53.00
    # BR 52.00

    # If country name does not exist, return '  NO price found'.

    #     >>> get_country_price('Mexico')
    #     53.00

    #     >>> get_country_price('Brazil')
    #     52.00

    #     >>> get_country_price('Trinidad')
    #     'No price found'
    # """
    mango_price_list= { 'Mexico': 53.00,
                        'Brazil': 52.00, 
                      }

    for country, price in mango_price_list.items():
        if country==country:
            list_fruit.append(mango_price_list[country])
    if list_fruit:
        return list_fruit
    else:
        list_fruit='No price found'
        return list_fruit

    print(get_fruit_price_by_country("Mexico"))


def wholesale_mango_order():
    """Assesses countries mangos available to purchase in."""

    # Check to make sure we've been passed an argument on the 
    # command line.  If not, display instructions.

    if len(sys.argv) < 2:
        show_help()
        sys.exit()

    # Get the name of the log file to open from the command line
    logfilename = sys.argv[1]

    # Open the log file
    f = open(fruit_flat_file.txt)

    # Read each line from the log file and process it

    for line in f:

        # Each line should be in the format:
        # <commodity>: <quantity>
        commodity, country = line.rstrip().split(' ')
        quantity = int(quantity)

        print "\n-----"
        print "Pricing for {} {}".format(quantity, commodity)
        print "-----\n"

        count = 0
        mangos = []

 def fruitpal(commodity, price, quantity):
    """Calculate total price of mangos, figuring in fixed and variable overhead.
    >>> fruitpal(mango, 53, 405)
    43.26
    >>> fruitpal(mango, 53, 405)
    420.0
    >>> fruitpal(mango, 53, 405)
    150.0
    >>> fruitpal(mango, 53, 405)
    65.0
    >>> fruitpal(mango, 53, 405)
    40.9
    >>> fruitpal(mango, 53, 405)
    135.3
    """
        MANGO BR 20 1.42
    #  price from country of origin + ( base_price * state_tax)  + all fees
    after_tax = base_price + ( base_price * state_tax )

    if country == "MX":
      # fixed_overhead = $32.00 per trade + 1.24 variable_overhead per ton
      after_v_overhead = quantity * 1.24 #variable overhead from file
      return after_v_overhead + fixed_overhead #fixed overhead from file
      


wholesale_mango_order()
