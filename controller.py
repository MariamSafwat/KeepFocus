from database.modelsfun import *
from backend import *

def main():

    progTexts = returnProgramTexts()
    print(extract_txt('images/Shot4.png',progTexts))

    progImgs = returnProgramImages()
    print("---------------------------")
    print(progImgs)


main()