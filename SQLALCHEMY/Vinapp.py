import pandas as pd
from flask import Flask , jsonify
import numpy as np
import matplotlib.pyplot as plt


import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

import datetime as dt
from datetime import timedelta

#################################################
# Database Setup
#################################################

# Create engine
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station


#################################################
# Flask Setup
#################################################

app = Flask(__name__)

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"/api/v1.0/precipitation<br/>"
        f'/api/v1.0/stations<br/>'
        f'/api/v1.0/tobs<br/>'
        f'/api/v1.0/<start>'
        f'/api/v1.0/<start>/<end>'
    )
@app.route('/api/v1.0/precipitation')
def precipitation():
    session = Session(engine)
    max_date=session.query(func.max(Measurement.date)).scalar()
    max_date = datetime.datetime.strptime(max_date, "%Y-%m-%d")
    oneyrolddate =max_date -timedelta(days=366)
    que_precip = session.query(Measurement.date,Measurement.prcp).filter((Measurement.date) > oneyrolddate).all()
    precipitation_list = []
    for date, precepetation in que_precip:
        precipitation_dict ={}
        precepetation_dict["Date"] = date
        precipitation_dict['Precipitation']= precp
        precipitation_list.append(precipitation_dict)
    
    return jsonify(precipitation_list)

@app.route('/api/v1.0/stations')
def stations():
    session = Session(engine)
    allstations = session.query(Station.station).all()
    station_list =[]
    for station in allstations:
        station_dict ={}
        station_dict["Stations"]=station
        station_list.append(station_dict)
    return jsonify(station_list)

@

if __name__ == '__main__':
    app.run(debug=True)



