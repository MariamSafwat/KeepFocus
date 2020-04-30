import sys
from PyQt5 import QtGui , QtWidgets
from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication, QVBoxLayout, QFormLayout, QLabel
from PyQt5.QtCore import QTimer
from database.modelsfun import *
import datetime


class ProgressBar(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.widget = QWidget(self)
        self.widget.setObjectName("main")
        self.widget.setStyleSheet("""
                    QWidget#main{
                        border:1px solid #148CD2;
                        border-radius:10px;
                    }
        """)

        self.progressBar = []        
        self.line = QFormLayout(self)
        self.line.setContentsMargins(20,20,20,20)
        self.line.setSpacing(30)

        today = datetime.date.today()
        Day = selectday(today)
        totalTime = max(Day['totalTime'],1)
        programs = Day['allPrograms']
        sorteddata = sorted(programs.items(),key=lambda x: -x[1])[:6]
        
        count = 0
        for prog in sorteddata:
            self.progressBar.append(QProgressBar())
            self.progressBar[count].setValue(prog[1]/totalTime *100)
            self.line.addRow(QLabel(prog[0]),self.progressBar[count])
            count += 1

        timer = QTimer(self)
        timer.timeout.connect(self.updateOnTime)
        timer.start(1000) # update every second

        self.widget.setLayout(self.line)      
        self.widget.setFixedSize(400,300)

    def updateOnTime(self):

        today = datetime.date.today()
        Day = selectday(today)
        totalTime = max(Day['totalTime'],1)
        programs = Day['allPrograms']
        sorteddata = sorted(programs.items(),key=lambda x: -x[1])[:6]

        
        count = self.line.rowCount()
        for i in range(0,count):
            self.line.removeRow(0)
            
       
        self.progressBar = []        
        count = 0
        for prog in sorteddata:
            self.progressBar.append(QProgressBar())
            self.progressBar[count].setValue(prog[1]/totalTime * 100)
            self.line.insertRow(count,QLabel(prog[0]),self.progressBar[count])
            count += 1
