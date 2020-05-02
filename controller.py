from database.modelsfun import *
from backend import *
from backend.system_api import *


def TakeDecision() :
    last10min = session.query(Statistics).order_by(Statistics.id.desc()).limit(10)
    
    productiveCount = 0
    for min in last10min:
        if min.productive == Programsdata.DISTRACTIVE and min.timerison:
            productiveCount +=1
    
    if productiveCount > 6:
        sendNotification("Keep Focus","Shouldn't you be working !?")


def Classifier(timerison):
    screenshot = takeScreenshot()
    screenshot.save('images/current.png')

    progTexts = returnProgramTexts()
    text_dic = extract_txt('images/current.png',progTexts)
    # print("--------------------------------------")
    # print(text_dic)
    # print("--------------------------------------")

    #normalize(text_dic)

    # print(text_dic)
    # print("--------------------------------------")

    # progImgs = returnProgramImages()
    # img_dic = getmatches('images/current.png', progImgs)
    # print("--------------------------------------")
    # print(img_dic)
    # print("--------------------------------------")

    # normalize(img_dic)

    # print(img_dic)
    # print("--------------------------------------")

    # sum_dic = {}
    # for key in text_dic.keys():
    #     sum_dic[key] = text_dic[key] + img_dic[key]

    orderedTuplesOfText = sorted(text_dic.items() ,  key=lambda x: -x[1]  )
    most_text = orderedTuplesOfText[0][0]

    # orderedTuplesOfImg = sorted(img_dic.items() ,  key=lambda x: -x[1]  )
    # most_img = orderedTuplesOfImg[0][0]

    # orderedTuplesOfTuple = sorted(sum_dic.items() ,  key=lambda x: -x[1]  )
    # most_Sum = orderedTuplesOfImg[0][0]

    updateOnScreenshoot(timerison,most_text)
    TakeDecision()


def normalize (dict_x):
    dict_values = dict_x.values()
    dict_min = min(dict_values)
    dict_max = max(dict_values)

    if dict_max == 0:
        return 

    for key, value in dict_x.items():
        if dict_max == dict_min : 
            dict_x[key] = 1 
        else:
            dict_x[key] = ( (dict_x[key] - dict_min) / (dict_max - dict_min) )

