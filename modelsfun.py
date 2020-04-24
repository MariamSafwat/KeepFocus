from models import *
import datetime
import ast



def checkDay():
    '''
    this function checks the last saved day instacnce 
    in the database to make sure it's todays
    '''

    day = session.query(Day).first()
    today = datetime.date.today()
    if day.Date != today:
        # initDay()
        pass
