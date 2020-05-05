import sys
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt

class Tutorial(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
        
    def initUI(self):
        txt1 = "<html><head/><body><p>Start organizing your time by going to the Options Tab</p><p>You will find many Websites and Applications of different </p><p>Categories where you can choose which is Productive for you, </p><p>which is Destructive, and which is Neutral</p></html>"
        txt2 = "<html><head/><body><p>Whenever you are about to start working, go to the Dashboard </p><p>and press Start, KeepFocus will then start keeping track of your </p><p>activities to help you stay Productive.</p></body></html>"
        txt3 = "<html><head/><body><p>From the Pie Chart you can view all Categories </p><p>and see which one you spend most of your time on</p></body></html>"
        txt4 = "<html><head/><body><p>The Weekly Bar Chart shows you how much Productive </p><p>and how much Destructive time you had each day of the week</p></body></html>"
        txt5 = "<html><head/><body><p>If you need more Details to know which Program is Blocking </p><p>your Productivity, the Progress Bars will show you the Percentage </p><p>of Time spent on each Program</p></body></html>"

        img1 = QtGui.QPixmap('1.jpeg')
        img2 = QtGui.QPixmap('2.jpeg')
        img3 = QtGui.QPixmap('3.jpeg')
        img4 = QtGui.QPixmap('4.jpeg')
        img5 = QtGui.QPixmap('5.jpeg')
        
        def first_inst(event):
                text.setText(txt1)
                pix_space.setPixmap(img1)
                
                prevButton.setEnabled(False)
                nextButton.setEnabled(True)
                finishButton.setEnabled(False)

                nextButton.clicked.connect(sec_inst)

                
        def sec_inst(event):
                text.setText(txt2)
                pix_space.setPixmap(img2)
                
                prevButton.setEnabled(True)
                nextButton.setEnabled(True)
                finishButton.setEnabled(False)

                prevButton.clicked.connect(first_inst)
                nextButton.clicked.connect(third_inst)

        def third_inst(event):
                text.setText(txt3)
                pix_space.setPixmap(img3)
                
                prevButton.setEnabled(True)
                nextButton.setEnabled(True)
                finishButton.setEnabled(False)

                prevButton.clicked.connect(sec_inst)
                nextButton.clicked.connect(fourth_inst)
        
        def fourth_inst(event):
                text.setText(txt4)
                pix_space.setPixmap(img4)
                
                prevButton.setEnabled(True)
                nextButton.setEnabled(True)
                finishButton.setEnabled(False)

                prevButton.clicked.connect(third_inst)
                nextButton.clicked.connect(fifth_inst)

        def fifth_inst(event):
                text.setText(txt5)
                pix_space.setPixmap(img5)
                
                prevButton.setEnabled(True)
                nextButton.setEnabled(False)
                finishButton.setEnabled(True)

                prevButton.clicked.connect(fourth_inst)
                finishButton.clicked.connect(finish)                
                
        def finish(event):
                self.close()
                

        prevButton = QPushButton("Prev")
        nextButton = QPushButton("Next")
        finishButton = QPushButton("Finish")
        
        prevButton.setFixedWidth(100)
        nextButton.setFixedWidth(100)
        finishButton.setFixedWidth(100)
        
        prevButton.setFixedHeight(30)
        nextButton.setFixedHeight(30)
        finishButton.setFixedHeight(30)

        prevButton.setEnabled(False)
        finishButton.setEnabled(False)
        
        
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(prevButton)
        hbox.addWidget(nextButton)
        hbox.addWidget(finishButton)
        
        
        vbox = QVBoxLayout()
        

        hbox1 = QHBoxLayout()
        text = QLabel(txt1)
        text.setFont(QFont('Arial', 11))
        text.setAlignment(Qt.AlignCenter)
        hbox1.addWidget(text)
        hbox1.setContentsMargins(80, 0, 80, 80)

        hbox2 = QHBoxLayout()
        #hbox.addStretch(1)
        
        pix_space = QLabel(self)
        
        pix_space.setScaledContents(True) 
        pix_space.setPixmap(img1)
        
        hbox2.addWidget(pix_space)
        hbox2.setContentsMargins(70, 0, 70, 0)
        #hbox2.setSpacing(100)
        

        vbox.addLayout(hbox2) #img
        vbox.addLayout(hbox1) #text
        vbox.addLayout(hbox) #buttons
        
        self.setLayout(vbox)

        nextButton.clicked.connect(sec_inst)
        #finishButton.clicked.connect(finish)
        
        self.setFixedSize(600,550)
        self.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet("background-color:white ")
        self.setWindowTitle('Welcome')    
        self.show()
        
        
    
