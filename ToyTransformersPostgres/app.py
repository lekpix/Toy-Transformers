from flask import Flask, jsonify, render_template, request
import numpy as np
from  postgres_pwd import pwd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
connstr=f"postgres:{pwd}@localhost:5432/ToyTransformer_DB"
engine=create_engine(f'postgresql://{connstr}')

# reflect an existing database into a new model
base = automap_base()
# reflect the tables
base.prepare(engine, reflect=True)
# Save reference to the table
Toy=base.classes.toy_tb

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

################Return the JSON representation of your dictionary.

@app.route("/toy")
def toys():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    results = session.query(Toy.name,Toy.toyname).all()

    session.close()

    toy_data = []
    for name, toyname in results:
        toy_dict = {}
        toy_dict["name"] = name
        toy_dict["toyname"] = toyname
        toy_data.append(toy_dict)
        
    return jsonify(toy_data)

# //Adding data
@app.route('/index.html', methods=['POST'])
def my_form_post():
    if request.method == "POST":
        session = Session(engine)
        name = request.form.get('name')
        toyname=request.form.get('toyname')
        # toyname="Volcanicus"
        addtoy = Toy(name=name, toyname=toyname)
        # session.add(text)
        session.add(addtoy)
        session.flush()
        session.commit()    
        session.close()
    # flash('Record was successfully added')
        # return "Your name is "+name + toyname
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)
