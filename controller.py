from database.modelsfun import *

def main():
    texts = returnProgramTexts()
    
    for key , value in texts.items():
        print(f"{key: } {value}")
        print("-----------------------------------")

main()