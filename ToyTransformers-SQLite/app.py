# from curses import flash
from flask import Flask, jsonify, render_template, request, redirect, url_for
from matplotlib import units
import numpy as np
# from  postgres_pwd import pwd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
# connstr=f"postgres:{pwd}@localhost:5432/ToyTransformer_DB"
# engine=create_engine(f'postgresql://{connstr}')
engine=create_engine("sqlite:///toyinventory.db",echo=False)
conn = engine.connect()
# reflect an existing database into a new model
base = automap_base()
# reflect the tables
base.prepare(engine, reflect=True)
# Save reference to the table
Toy = base.classes.toyinventory

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def HomePage():
    
    return render_template('index.html')
@app.route("/index.html")
def Home():
    
    return render_template('index.html')
@app.route("/additem")
def additem():
    
    return render_template('additem.html')
@app.route("/edititem")
def toyedit():

    return render_template('edititem.html')


################Return the JSON representation of your dictionary.

@app.route("/toytable")
def toys():
    # Create our session (link) from Python to the DB
    session = Session(bind=engine)
    
    results = session.query(Toy.suppliername,Toy.toyname,Toy.price,Toy.unit,Toy.productlocation).all()

    session.close()

    toy_data = []
    for suppliername, toyname,price,unit,productlocation in results:
        toy_dict = {}
        toy_dict["Supplier"] = suppliername
        toy_dict["Product"] = toyname
        toy_dict["Price"] = price
        toy_dict["Unit"] = unit
        toy_dict["Location"] = productlocation
        toy_data.append(toy_dict)
        
    toytable=jsonify(toy_data)
    return toytable

# //Adding data
@app.route('/additem', methods=['POST'])
def my_form_post():
    if request.method == "POST":
        session = Session(engine)
        # suppliername = request.form['suppliername']///this also works
        
        suppliername = request.form.get('suppliername')
        toyname=request.form.get('toyname')
        price=request.form.get('price')
        unit=request.form.get('unit')
        productlocation=request.form.get('productlocation')
        
       
        NewItem=Toy(suppliername=suppliername,toyname=toyname,price=price,unit=unit,productlocation=productlocation)
        session.add(NewItem)
        
         # session.flush()
        session.commit()    
        session.close()

        return "Data Added"
    return render_template('additem.html')

if __name__ == "__main__":
    app.run(debug=True)
