import sys
from PyQt5 import QtGui , QtWidgets
from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication, QVBoxLayout, QFormLayout, QLabel
from PyQt5.QtCore import QBasicTimer
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


        layout = QVBoxLayout(self)
        layout.setContentsMargins(20,20,20,20)
        progressBar = []        


        today = datetime.date.today()
        Day = selectday(today)
        print(Day)
        programs = Day['allPrograms']
        sorteddata = sorted(programs.items(),key=lambda x: -x[1])[:6]
        
        count = 0
        for prog in sorteddata:
            line = QFormLayout(self)
            progressBar.append(QProgressBar())
            line.addRow(QLabel(prog[0]),progressBar[count])
            line.setSpacing(30)
            progressBar[count].setValue(prog[1])
            layout.addItem(line)
            count += 1

        self.widget.setLayout(layout)      
        self.widget.setFixedSize(400,300)
