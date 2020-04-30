from PyQt5 import QtGui , QtWidgets
from PyQt5.QtChart import QChart, QChartView, QValueAxis, QBarCategoryAxis, QBarSet, QBarSeries
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout 
from database.modelsfun import *


class BarChart(QtWidgets.QWidget):
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
        
        data0 = [1,6,3,2,8,6,7]
        data1 = [5,8,2,6,1,2,4]
        
        
        self.create_barchart(data0,data1)

        layout = QVBoxLayout (self)
        layout.setContentsMargins(5,5,5,5)
        layout.addWidget(self.chartview)
        self.widget.setLayout(layout)
        self.widget.setFixedSize(500,300)
        
    def create_barchart(self, data0, data1):
        set0 = QBarSet('PRODUCTIVE')
        set1 = QBarSet('DESTRUCTIVE')
        
        set0.append(data0)
        set1.append(data1)
        
        series = QBarSeries()
        
        series.append(set0)
        series.append(set1)
        
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle('Weekly Bar Chart')
        chart.setAnimationOptions(QChart.SeriesAnimations)
        
        days = ('Mon', 'Teu', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
        
        axisX = QBarCategoryAxis()
        axisX.append(days)
        
        axisY = QValueAxis()
        axisY.setRange(0, 24)
        
        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
        self.chartview = QChartView(chart)
        
        self.chartview.setRenderHint(QPainter.Antialiasing)
        
    
