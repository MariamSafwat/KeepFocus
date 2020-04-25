from models import *
import datetime
import ast
import csv

def selectday(sdate):
    day=session.execute("SELECT * from Day where date=:d",{'d':sdate}).first()
    programs_dic = {}
    final_dic = {}
    programs = day.allprograms
    programs = ast.literal_eval(programs)

    for program in programs:
        day=session.execute("SELECT name from Programsdata where id=:d",{'d':program}).first()
        category_dic[day[0]]=programs[program]
    
    final_dic['date']=sdate
    final_dic['allcategory']=category_dic
    final_dic['totalTime']=day.totalTime
    final_dic['timerOnTime']=day.timerOnTime
    return final_dic
    



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
    programs_list=session.execute("SELECT * from Programsdata").fetchall()
    programs_dic={}
    
    for program in programs_list:
        programs_dic[program.id]=0
    
    today=datetime.date.today()
    newday=Day(date=today,allCatagory=str(programs_dic),totalTime=0,timerOnTime=0)
    session.add(newday)
    session.commit()


def returnProgramTexts():
    '''
    Return A list of all programs text directory
    '''
    programs = session.query(Programsdata).all()
    
    dic = {}
    for program in programs:
        x = program.listoftext
        x = ast.literal_eval(x)
        dic[program.id]=x
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

def AddingPrpramsData(csv_path):
    '''
    this function reads data from csv file
    '''
    f = open(csv_path)
    reader = csv.reader(f)
    
    for name, listoftext, listofimage,productive in reader:
        ProgData = Programsdata(name=name,listoftext=listoftext,listofimage=listofimage , productive=productive)
        session.add(ProgData)
    session.commit()

    