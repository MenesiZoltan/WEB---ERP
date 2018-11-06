from flask import Flask, render_template, url_for, redirect, request, Blueprint
import data_manager

app = Flask(__name__)

@app.route('/')
def route_home():
    return render_template('home.html')


####   Imports for running different modules   ####

from accounting.routes_accounting import *
from customer_relations.routing_crm import *
from human_resources.routing_hr import *
from inventory.routing_inventory import *
from sales.routing_sales import *
from store.routing_store import *


if __name__ == '__main__':
    app.run(debug=True)
