from modelsfun import *


'''
day=Day(date=datetime.date.today(),allCatagory="",totalTime=0,timerOnTime=0)
session.add(day)
session.commit()

s=session.query(Statistics).first()
day.statistics.append(s)
'''
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




print(returnProgramTexts())