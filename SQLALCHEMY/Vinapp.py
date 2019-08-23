import pandas as pd
from flask import Flask , jsonify, request
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
        f'Available Routes: <br/>'
        f'<a href="/api/v1.0/precipitation">/api/v1.0/precipitation</a><br/>'
        f'<a href="/api/v1.0/stations">/api/v1.0/stations</a><br/>'
        f'<a href="/api/v1.0/tobs">/api/v1.0/tobs</a><br/><br/>'
        f'<div> Use following link if you have a date range. \
                Copy paste the link below after the server address. \
                Enter the start date in yyyy-mm-dd format <br/>\
                For example : Enter in following way after the server address<br/>\
                /api/v1.0/2013-01-01        </div><br/>'
        f'/api/v1.0/<br/><br/><br/><br/>'        
        f'<div> Use following link if you have a date range. \
                Copy paste the link below after the server address. \
                Enter the start and end date in yyyy-mm-dd format <br/>\
                For example : Enter in following way after the server address<br/>\
                /api/v1.0/2013-01-01/2013-12-31       </div><br/>'
        f'/api/v1.0/'
    )
@app.route('/api/v1.0/precipitation')
def precipitation():
    session = Session(engine)
    max_date=session.query(func.max(Measurement.date)).scalar()
    max_date = dt.datetime.strptime(max_date, "%Y-%m-%d")
    oneyrolddate =max_date -timedelta(days=366)
    que_precip = session.query(Measurement.date,Measurement.prcp).filter((Measurement.date) > oneyrolddate).all()
    precipitation_list = []
    for date, prcp in que_precip:
        precipitation_dict ={}
        precipitation_dict["Date"] = date
        precipitation_dict['Precipitation']= prcp
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

@app.route('/api/v1.0/tobs')
def temperatures():
    session = Session(engine)
    
    max_date=session.query(func.max(Measurement.date)).scalar()
    max_date = dt.datetime.strptime(max_date, "%Y-%m-%d")
    oneyrolddate =max_date -timedelta(days=366)
    que_temps = session.query(Measurement.date,Measurement.tobs).filter((Measurement.date) > oneyrolddate).all()
    temp_list = []
    for date, tobs in que_temps:
        temp_dict ={}
        temp_dict["Date"] = date
        temp_dict['Temperature']= tobs
        temp_list.append(temp_dict)
    
    return jsonify(temp_list)  

@app.route ('/api/v1.0/<start>/<end>')
def start_end_date (start,end):
    session = Session(engine)

    TMIN = session.query(func.min(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).scalar()
    TAVG = session.query(func.avg(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).scalar()
    TMAX = session.query(func.max(Measurement.tobs)).filter(Measurement.date >= start).filter(Measurement.date <= end).scalar()
    temp_stats = [TMIN, TAVG, TMAX]
    return jsonify(temp_stats)

@app.route ('/api/v1.0/<start>')
def start_date (start):
    session = Session(engine)
    
    TMIN = session.query(func.min(Measurement.tobs)).filter(Measurement.date >= start).scalar()
    TAVG = session.query(func.avg(Measurement.tobs)).filter(Measurement.date >= start).scalar()
    TMAX = session.query(func.max(Measurement.tobs)).filter(Measurement.date >= start).scalar()
    temp_stats = [TMIN, TAVG, TMAX]
    return jsonify(temp_stats)
    


if __name__ == '__main__':
    app.run(debug=True)



