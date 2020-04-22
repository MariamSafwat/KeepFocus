from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5 import QtGui




class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pie Chart")
        self.setGeometry(100,100, 1280,600)

        self.show()
        data = {"Social media": 50,"Educational": 20,"News": 10,"Other": 20,}
        self.create_piechart(data)



    def create_piechart(self,data):
        #data = {"Social media": 50,"Educational": 20,"News": 10,"Other": 20,}
        series = QPieSeries()

        for name, value in data.items():
            _slice = series.append(name, value)
            _slice.setLabelVisible(True) # can be removed if unnecessary
            #_slice.setBrush(color)
            



        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.createDefaultAxes()
        chart.setAnimationOptions(QChart.SeriesAnimations)
        chart.setTitle("Pie Chart")

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chartview = QChartView(chart)
        chartview.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(chartview)





App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec_())
