from PyQt5 import QtGui , QtWidgets
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QWidget, QHBoxLayout 
from database.modelsfun import selectday
import datetime


class PieChart(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.setObjectName("main")
        self.setStyleSheet("""
                    QWidget{
                        border:1px solid #148CD2;
                        border-radius:10px;
                    }
        """)
        self.create_piechart()

        timer = QTimer(self)
        timer.timeout.connect(self.redraw)
        timer.start(5*60*1000) # update every second

        layout = QHBoxLayout (self)  
        layout.setContentsMargins(5,5,50,5)      
        layout.addWidget(self.chartview)

        self.setLayout(layout)
        self.setFixedSize(500,400)

    def create_piechart(self):
        today = datetime.date.today()
        Day = selectday(today)
        catogeries = Day['allCategory']
        catogeries = dict(sorted(catogeries.items(),key=lambda x: -x[1])[:5])
        print(f"--------------------{catogeries}--------")
        series = QPieSeries()

        tot_val = 0
        for name, value in catogeries.items():
            tot_val += value

        for name, value in catogeries.items():
            _slice = series.append(name, 100*(value/tot_val))
            _slice.setLabelVisible(True) # can be removed if unnecessary
            
        self.chart = QChart()
        self.chart.legend().hide()
        self.chart.addSeries(series)
        self.chart.createDefaultAxes()
        self.chart.setAnimationOptions(QChart.SeriesAnimations)
        self.chart.setTitle("Categories")

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        self.chartview = QChartView(self.chart)
        self.chartview.setRenderHint(QPainter.Antialiasing)

    def redraw(self):   
        # remove pieChart
        self.chart.removeAllSeries()

        today = datetime.date.today()
        Day = selectday(today)
        catogeries = Day['allCategory']
        catogeries = dict(sorted(catogeries.items(),key=lambda x: -x[1])[:5])
        print(f"--------------------{catogeries}--------")
        series = QPieSeries()

        tot_val = 0
        for name, value in catogeries.items():
            tot_val += value

        for name, value in catogeries.items():
            _slice = series.append(name, 100*(value/tot_val))
            _slice.setLabelVisible(True) # can be removed if unnecessary
            
        self.chart.addSeries(series)

        self.chartview.setChart((self.chart))
        self.chartview.setRenderHint(QPainter.Antialiasing)
        self.chartview.repaint()