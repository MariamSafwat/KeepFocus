# ------------------------------------------------- ----- 
# ---------------------- main.py ------------------- ---- 
# --------------------------------------------- --------- 
from  PyQt5.QtWidgets  import * 
from  PyQt5.uic  import  loadUi
from PyQt5.QtChart import QChart, QChartView, QPieSeries, QPieSlice

from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from PyQt5 import QtGui

     
class  MatplotlibWidget ( QMainWindow ):
    
    def  __init__ ( self ):
        
        QMainWindow . __init__ ( self )

        loadUi ( "qt_designer.ui" , self )

        self . setWindowTitle ( "Pie Chart" )

        self . update_graph()

        #self . addToolBar ( NavigationToolbar ( self . MplWidget . canvas ,  self ))


    def  update_graph ( self ):
        data = {"Social media": 50,"Educational": 20,"News": 10,"Other": 20,}
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

        

app  =  QApplication ([]) 
window  =  MatplotlibWidget () 
window . show () 
app . exec_ ()
