from database.modelsfun import *
from backend import *
from backend.system_api import *


def TakeDecision(timerison) :
    last10min = session.query(Programsdata).order_by(a.id.desc()).limit(10)
    
    productiveCount = 0
    for min in last10min:
        if min.productive == Programsdata.DISTRACTIVE:
            productiveCount +=1
    
    if productiveCount > 6 and timerison:
        sendNotification("Keep Focus","Shouldn't you be working !?")



def Classifier():
    screenshot = takeScreenshot()
    screenshot.save('images/current.png')

    progTexts = returnProgramTexts()
    text_dic = extract_txt('images/current.png',progTexts)

    progImgs = returnProgramImages()
    img_dic = getmatches('images/current.png', progImgs)

    sum_dic = {}
    for key in text_dic.keys():
        sum_dic[key] = text_dic[key] + img_dic[key]

    orderedTuplesOfText = sorted(text_dic.items() ,  key=lambda x: -x[1]  )
    most_text = orderedTuplesOfText[0][0]

    orderedTuplesOfImg = sorted(img_dic.items() ,  key=lambda x: -x[1]  )
    most_img = orderedTuplesOfImg[0][0]

    orderedTuplesOfTuple = sorted(sum_dic.items() ,  key=lambda x: -x[1]  )
    most_Sum = orderedTuplesOfImg[0][0]
    updateOnScreenshoot(True,1)
    
    return most_Sum
