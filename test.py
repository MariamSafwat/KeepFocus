from modelsfun import *
from sqlalchemy import func
import datetime

'''
c={1:2,2:1}
datestr='2020-04-23'
date=datetime.datetime.strptime(datestr, '%Y-%m-%d').date()
day=Day(date=date,allCatagory=str(c),totalTime=0,timerOnTime=0)
session.add(day)
session.commit()
'''

'''
datestr='2020-04-24'
date=datetime.datetime.strptime(datestr, '%Y-%m-%d').date()
d=session.execute("SELECT * from Day where date=:d",{'d':date}).first()

s=session.execute("SELECT * from statistics ").first()
print(d)
print(s)
d.statistics.append(s)
'''


'''
d=Day()
s=Statistics()
d.statistics.append(s)
'''



#d.statistics.append(s)

#insert in programsdata
'''
dic = ['fb','face','FB']
strdic = str(dic)
p=Programsdata(name='Facebook',listoftext=strdic,listofimage=0,productive=0)
session.add(p)
session.commit()
dic = ['WA','wa','whats']
strdic = str(dic)
p=Programsdata(name='whatsapp',listoftext=strdic,listofimage=0,productive=0)
session.add(p)
session.commit()
'''

#d=session.query(Day).all()

nowdate=datetime.date.today()

#datestr='2020-04-23'
#date=datetime.datetime.strptime(datestr, '%Y-%m-%d').date()
#selectday(date)


#print(returnProgramTexts())

#AddingPrpramsData('prog.csv')
date=datetime.date.today()
initday()