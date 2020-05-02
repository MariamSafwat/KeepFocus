from PyQt5 import QtGui , QtWidgets
from PyQt5.QtChart import QChart, QChartView, QValueAxis, QBarCategoryAxis, QBarSet, QBarSeries
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout 
from database.modelsfun import *
from datetime import date,timedelta
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
        

        today = datetime.date.today()
        days = []
        today = datetime.date.today()
        data0 = []
        data1 = []
        for single_date in (today + timedelta(n) for n in range(7)):
            try:
                current = selectday(single_date)
                data0.append(current['distructive_time']/ current['totalTime'] * 100)
                data1.append(current['productive_time']/ current['totalTime'] * 100)

            except:
                data0.append(0)
                data1.append(0)


        
        
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
        

        today = datetime.date.today()
        days = []
        today = datetime.date.today()
        for single_date in (today + timedelta(n) for n in range(7)):
            days.append(single_date.strftime("%AAA"))

        
        axisX = QBarCategoryAxis()
        axisX.append(days)
        
        axisY = QValueAxis()
        axisY.setRange(0, 100)
        
        chart.addAxis(axisX, Qt.AlignBottom)
        chart.addAxis(axisY, Qt.AlignLeft)
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)
        self.chartview = QChartView(chart)
        
        self.chartview.setRenderHint(QPainter.Antialiasing)
        
    
