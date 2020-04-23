import sys
from PyQt5 import QtGui , QtWidgets
from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication, QVBoxLayout, QFormLayout, QLabel
from PyQt5.QtCore import QBasicTimer


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

        for i in range(0,5):
            line = QFormLayout(self)
            progressBar.append(QProgressBar())
            line.addRow(QLabel('ProgName'),progressBar[i])
            line.setSpacing(30)
            progressBar[i].setValue(50)
            layout.addItem(line)

        self.widget.setLayout(layout)      
        self.widget.setFixedSize(500,400)
