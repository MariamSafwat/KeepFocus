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
    if day is None:
        initday()
    elif day.date != today:
        initday()


def initday():
    '''
    this function initialize new day
    '''
    today=datetime.date.first()
    newday=Day(date=today,allCatagory="",totalTime=0,timerOnTime=0)
    session.add(newday)
    session.commit()


def returnProgramTexts():
    '''
    Return A list of all programs text directory
    '''
    programs = session.query(Programsdata).all()
    
    dic = {}
    for program in programs:
        dic[program.id] = program.listoftext

    return dic


def returnProgramImages():
    '''
    Return A list of all programs images directory
    '''
    programs = session.query(Programsdata).all()
    
    dic = {}
    for program in programs:
        dic[program.id] = program.listofimage

    return dic


def updateOnScreenshoot(timerOn, program):
    '''
    takes the classified programs and make new statistcs instance and update the day data
    '''
    checkDay()

    programIns = session.query(Programsdata).filter(id = program)[0]
    produciv = programIns.productive

    newStatistics = Statistics(dateAndTime = datetime.datetime.now(),
                             timer = timerOn, programe = program, producive = produciv  )
    session.add(newStatistics)

    day = session.query(Day).first()
    day.statistics.append(newStatistics)
    day.totalTime += 1
    if timerOn == True:
        day.timerOnTime += 1

    dic = day.allCatagory
    dic = ast.literal_eval(dic)
    dic[program] = int(dic[program]) + 1
    day.allCatagory = str(dic)
    session.commit()