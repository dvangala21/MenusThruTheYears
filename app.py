
# This app is currently broken. We attempted to connect to the Google Cloud but did not get time to fix the flask routes. 

import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from db_config import DATABASE_URL
# pip install mysqlclient

app = Flask(__name__)


#################################################
# Database Setup
#################################################

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/Dish.sqlite"
# db = SQLAlchemy(app)

# reflect an existing database into a new model
Base = automap_base()

#"sqlite:///Dish.db"
engine = create_engine(DATABASE_URL)

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Dish = Base.classes.Dish
# Menu = Base.classes.menu
# Menu_Item = Base.classes.Menu_Item
# Menu_Page = Base.classes.Menu_Page


@app.route("/")
def index():
    """Return the homepage."""
    return render_template("index.html")


# @app.route("/Dish")
# def names():
#     """Return Column Headers."""

#     # Use Pandas to perform the sql query
#     stmt = db.session.query(Dish).statement
#     df = pd.read_sql_query(stmt, db.session.bind)

#     # Return a list of the column names (sample names)
#     return jsonify(list(df.columns)[2:])

@app.route("/hello")
def hello(): 
    dish = Dish.NAME
    return jsonify(Dish.NAME)


@app.route("/Dish/<name>")
def dish(name):
    """Return the data for a given Dish Name."""
    
    sel = [
        Dish.NAME,
        Dish.MENUS_APPEARED,
        Dish.FIRST_APPEARED, 
        Dish.LAST_APPEARED, 
        Dish.LOWEST_PRICE,
        Dish.HIGHEST_PRICE
    ]

    results = db.session.query(*sel).filter(Dish.Name == name).all()

    # Create a dictionary entry for each row of metadata information
    Dish_data = {}
    for result in results:
        Dish_data["NAME"] = result[0]
        Dish_data["MENUS_APPEARED"] = result[1]
        Dish_data["LOWEST_PRICE"] = result[2]
        Dish_data["HIGHEST_PRICE"] = result[3]

    print(Dish_data)
    return jsonify(Dish_data)

# @app.route("/Menu/<name>")
# def menu(name):
#     """Return the data for a given Menu Name."""
#     sel = [
#         Menu.NAME,
#         Menu.SPONSOR,
#         Menu.DATE, 
#         Menu.LOCATION, 
#         Menu.CURRENCY,
#         Menu.PAGE_COUNT, 
#         Menu.DISH_COUNT
#     ]

#     results = db.session.query(*sel).filter(Menu.Name == name).all()

#     # Create a dictionary entry for each row of metadata information
#     Menu_Data = {}
#     for result in results:
#         Menu_Data["NAME"] = result[0]
#         Menu_Data["SPONSOR"] = result[1]
#         Menu_Data["DATE"] = result[2]
#         Menu_Data["LOCATION"] = result[3]
#         Menu_Data["CURRENCY"] = result[4]
#         Menu_Data["PAGE_COUNT"] = result[5]
#         Menu_Data["DISH_COUNT"] = result[6]

#     print(Menu_Data)
#     return jsonify(Menu_Data)




if __name__ == "__main__":
    app.run()
