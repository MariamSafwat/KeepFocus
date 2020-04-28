from .model import *
import datetime
import ast
import csv


def selectday(sdate):
    sdate = str(sdate)
    day =session.execute("SELECT * from Day where date=:d",{'d':sdate}).first()
    programs_dic = {}
    final_dic = {}
    category_dic  = {}
    programs = day.allPrograms
    programs = ast.literal_eval(programs)

    for program in programs:
        name = session.query(Programsdata).get(program).name
        print(programs[program])
        category_dic[name] = programs[program]
    
    final_dic['date']=sdate
    final_dic['allPrograms '] = category_dic
    final_dic['totalTime'] = day.totalTime
    final_dic['timerOnTime'] = day.timerOnTime
    return final_dic
    


def checkDay():
    '''
    this function checks the last saved day instacnce 
    in the database to make sure it's todays
    '''
    day = session.query(Day).order_by(Day.id.desc()).first()
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
    
    today = datetime.date.today()
    newday=Day(date=today,allPrograms=str(programs_dic),totalTime=0,timerOnTime=0)
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

    programIns = session.query(Programsdata).get(program)
    produciv = programIns.productive

    newStatistics = Statistics(dateAndTime = datetime.datetime.now(),
                             timer = timerOn, programe = program, productive = produciv  )
    session.add(newStatistics)

    day = session.query(Day).order_by(Day.id.desc()).first()
    day.statistics.append(newStatistics)
    day.totalTime += 1
    if timerOn == True:
        day.timerOnTime += 1
    session.commit()

    dic = day.allPrograms
    dic = ast.literal_eval(dic)
    dic[program] = int(dic[program]) + 1
    day.allPrograms = str(dic)
    session.commit()


def AddingProgramsData(csv_path):
    '''
    this function reads data from csv file
    '''
    f = open(csv_path)
    reader = csv.reader(f)
    
    for name, listoftext, listofimage,productive,category_id in reader:
        ProgData = Programsdata(name=name,listoftext=listoftext,listofimage=listofimage , productive=productive , prog_category=category_id)
        session.add(ProgData)
    session.commit()


def add_category(csv_path):
    '''
    this function reads data from csv file
    '''
    f = open(csv_path)
    reader = csv.reader(f)
    
    for name in reader:
        category = Category(name=name[0])
        session.add(category)
    session.commit()

def returnProgramsCategory(program):
    '''
    return the category fo any program
    '''
    categoryName=session.execute("Select category.name from category Inner join Programsdata ON Programsdata.name=:p and Programsdata.prog_category=category.id",{'p':program}).fetchall()[0]
    return categoryName

def returnCategoryID(category):
    categoryID=session.execute("Select category.id from category WHERE category.name=:cat",{'cat':category}).fetchall()[0]
    print(categoryID)

    
def returnAllprogramStatus():
    return dict(Programsdata.STATUS)

# test code 

# add_category('database/category.csv')

# AddingProgramsData('database/prog.csv')

