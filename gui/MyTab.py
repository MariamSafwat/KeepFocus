from PyQt5 import QtCore, QtGui, QtWidgets 

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QLabel, QFormLayout, QPushButton, QToolButton
from PyQt5.QtCore import pyqtSlot , Qt, QSize
from PyQt5.QtGui import QIcon , QFont, QPixmap, QPalette, QBrush, QColor

from MyTable import MyTableWidget
from myPie import PieChart
from myProgBar import ProgressBar
from myBar import BarChart
from myTimer import Timer

class MyTabWidget(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        # Initialize tab screen
        self.tabs = TabWidget()
        self.tabs.setStyleSheet("background:white")
        self.dashboard = QWidget()
        self.options = QWidget()
        self.tabs.setMinimumSize(700,600)

        self.tabs.setIconSize(QSize(30,30))        
    

        # Add tabs
        self.tabs.addTab(self.dashboard,QtGui.QIcon("dashboard_grey.png"),"Dashboard")
        self.tabs.addTab(self.options,QtGui.QIcon("settings_grey.png"),"Options")
        # Create option tab
        self.tabs.setTabToolTip(1,'Customize your controls')

        self.options.layout = QHBoxLayout(self)
        self.options.layout.setContentsMargins(30,0,60,0);

        mytable = MyTableWidget()
        mytable.setStyleSheet("background-color:white")

        # Page title
        optionTitle =  QLabel("Review the list below and make sure the categories and scores feel correct for you")
        font1 = QFont ("sans-serif",16,QFont.Bold,True)
        optionTitle.setFont(font1)

        optionTitle.setContentsMargins(20,20,0,50)
        optionPage = QFormLayout()
        optionPage.setContentsMargins(0,0,0,0)
        
        optionPage.addRow(optionTitle)
        optionPage.addRow(mytable)

        self.options.layout.addItem(optionPage)        
        self.options.setLayout(self.options.layout)
        
        # Create dashboard tab 
        self.tabs.setTabToolTip(0,'See your productivity')
        self.dashboard.layout = QHBoxLayout(self)
        self.dashboard.layout.setContentsMargins(50,20,0,0);

        dashboard_page = QVBoxLayout()
        dashboard_page.setContentsMargins(0,0,0,0);
        pieChart = PieChart()
        progBar = ProgressBar()
        barChart = BarChart()
        timer = Timer()

        dashboard_page.addWidget(timer)
        dashboard_page.addWidget(pieChart)
        dashboard_page1 = QVBoxLayout()
        dashboard_page1.setContentsMargins(0,0,0,0);
        dashboard_page1.addWidget(progBar)
        dashboard_page1.addWidget(barChart)

        self.dashboard.layout.addLayout(dashboard_page)
        self.dashboard.layout.addLayout(dashboard_page1)
        

        self.dashboard.setLayout(self.dashboard.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
    

class TabWidget(QtWidgets.QTabWidget):
    def __init__(self, *args, **kwargs):
        QtWidgets.QTabWidget.__init__(self, *args, **kwargs)
        tabBar = TabBar(self)
        tabBar.setStyleSheet('''

            QTabWidget::pane { /* The tab widget frame */
                border-top: 2px solid #C2C7CB;
            }
            QTabWidget::tab-bar {
                left: 5px; /* move to the right by 5px */
            }
            /* Style the tab using the tab sub-control. Note that
                it reads QTabBar _not_ QTabWidget */
            QTabBar::tab {
                background-color:#22282d;
                color:#FFFFFF;
                min-width: 12ex;
                min-height: 12ex;
                text-align:left;
                padding: 5px;
                font-family:"Times New Roman", Times, serif;
                font-weight:bold;
                font-size:18px; 
                border:none;
                margin-right:1px;
            }
            QTabBar::tab:hover {
                background:#017ffc;
            }

            QTabBar::tab:selected {
                background-color:#017ffc;   
            }

            QTabBar::tab:!selected {
                
            }
        
        ''')

        self.setTabBar(tabBar)
        self.setTabPosition(QtWidgets.QTabWidget.West)


class TabBar(QtWidgets.QTabBar):
    def tabSizeHint(self, index):
        s = QtWidgets.QTabBar.tabSizeHint(self, index)
        s.transpose()
        return s

    
    def paintEvent(self, event):
        painter = QtWidgets.QStylePainter(self)
        opt = QtWidgets.QStyleOptionTab()

        for i in range(self.count()):
            self.initStyleOption(opt, i)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabShape, opt)
            painter.save()

            s = opt.rect.size()
            s.transpose()
            r = QtCore.QRect(QtCore.QPoint(), s)
            r.moveCenter(opt.rect.center())
            opt.rect = r

            c = self.tabRect(i).center()
            painter.translate(c)
            painter.rotate(90)
            painter.translate(-c)
            painter.drawControl(QtWidgets.QStyle.CE_TabBarTabLabel, opt);
            painter.restore()
