from database.modelsfun import *
from backend import *

def main():

    progTexts = returnProgramTexts()
    print(extract_txt('images/Shot4.png',progTexts))

    progImgs = returnProgramImages()
    print(getmatches('images/Screenshot (56).png', progImgs))
    print("---------------------------")
    print(progImgs)


main()