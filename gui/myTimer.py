import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFormLayout, QLabel, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import QTimer, QTime, Qt
from controller import Classifier


class Timer(QWidget):
    def __init__(self):
        super().__init__()
        
        self.widget = QWidget(self)
        self.widget.setObjectName("main")
        self.widget.setStyleSheet("""
                    QWidget#main{
                        border:1px solid #148CD2;
                        border-radius:10px;
                        margin:0
                    }
        """)

        layout = QVBoxLayout()
        
        fnt = QFont('Open Sans', 60, QFont.Bold)
        self.lbl = QLabel()
        self.lbl.setAlignment(Qt.AlignCenter)
 
        self.currentTime = QTime(0,0,0)
        self.lbl.setFont(fnt)
        
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000) # update every second

        self.btnStart = QPushButton('Start', self)
        self.btnStart.setStyleSheet(
            """
            QPushButton
            {
                margin-right:20px;
            }
            QPushButton:hover
            {
                background-color:#148CD2;
                border:none;
            }
            """)
        line = QFormLayout()
        line.setContentsMargins(0,20,0,0)
        self.msg = QLabel("Elapsed Time")
        fnt2 = QFont('Open Sans', 28)
        self.msg.setFont(fnt2)

        self.btnStart.setFixedSize(100,50)
        self.btnStart.clicked.connect(self.startProgress) 

        self.showTime()
        self.timerStatus = False

        line.addRow(self.btnStart,self.msg)

        layout.addWidget(self.lbl)
        layout.addItem(line) 

        self.widget.setLayout(layout)
        self.widget.setFixedSize(400,200)


        Classifiertimer = QTimer(self)
        Classifiertimer.timeout.connect(self.ClassifierRunner)
        Classifiertimer.start(5000) # update every second


    def showTime(self):
        if self.btnStart.text() == 'Stop':
            self.currentTime = self.currentTime.addSecs(1)
            displayTxt = self.currentTime.toString('hh:mm:ss')
            self.lbl.setText(displayTxt)
        else:
            displayTxt = self.currentTime.toString('hh:mm:ss')
            self.lbl.setText(displayTxt)

    def startProgress(self):
        if self.btnStart.text() == 'Start':
            self.btnStart.setText('Stop')
            self.timerStatus = True
        else:
            self.btnStart.setText('Start')
            self.currentTime = QTime(0,0,0)
            self.timerStatus = False
            
    def ClassifierRunner(self):
        print("/////////////////////////////////////////////////////////////////")
        Classifier(self.timerStatus)
        print('??????????????????????????????????????????????????????????????????')