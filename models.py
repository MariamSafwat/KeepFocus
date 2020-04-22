from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Flight(db.Model):
    __tablename__ = "statistics"
    id = db.Column(db.Integer, primary_key=True)
    DateAndTime = db.Column(db.DateTime, nullable=False)#data and time for screenshot
    Timebool = db.Column(db.Integer, nullable=False)#check if time on when screen shot have been taken
    Dictionary=db.Column(db.String, nullable=False)#output from image processing
    productive = db.Column(db.String, nullable=False)#check if image is productive or not
    


class Passenger(db.Model):
    __tablename__ = "programsdata"
    id = db.Column(db.Integer, primary_key=True)
    listoftext = db.Column(db.String, nullable=False)
    listofimage = db.Column(db.Integer, nullable=False)