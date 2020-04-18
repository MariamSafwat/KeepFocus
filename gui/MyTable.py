
from PyQt5 import QtCore, QtWidgets 
from PyQt5.QtWidgets import QWidget,QComboBox, QPushButton


class MyTableWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.table = QtWidgets.QTableWidget(3, 3, self)

        temp_database = [('google-chrome','BROWSERS'),
                            ('facebook','SOCIAL MEDIA'),
                            ('code','SOFTWARE DEV')
                        ]
        
        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                if col == 2:
                    prod_list = QComboBox()
                    prod_list.addItems(['PRODUCTIVE','NEUTRAL','DISTRACTING'])
                    prod_list.setStyleSheet("""
                        QComboBox{
                            border:none;
                            background-color:transparent;
                        }
                        QComboBox:selected{
                            background-color:#148CD2;
                        }
                    """)

                    self.table.setCellWidget(row, col, prod_list)
                else:    
                    item = QtWidgets.QTableWidgetItem('{}'.format(temp_database[row][col]))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setItem(row, col, item)
                self.table.setRowHeight(row,50)    

        
        self.table.setHorizontalHeaderLabels(
            'Activity|Catogery|Productivity'.split('|')) 
        self.table.horizontalHeader().setFixedHeight(50)

        self.table.setColumnWidth(0,300)   
        self.table.setColumnWidth(1,400)   
        self.table.setColumnWidth(2,400)   

        self.table.setStyleSheet('''QTableView  {border: none; }
            QScrollBar:horizontal {
                border: none;
                background: none;
                height: 15px;
                margin: 0px 26px 0 26px;
            }

            QScrollBar::handle:horizontal {
                background: #1a73aa;
                min-width: 26px;
            }

            QScrollBar::add-line:horizontal {
                background: none;
                width: 26px;
                subcontrol-position: right;
                subcontrol-origin: margin;
                
            }

            QScrollBar::sub-line:horizontal {
                background: none;
                width: 26px;
                subcontrol-position: top left;
                subcontrol-origin: margin;
                position: absolute;
            }

            QScrollBar:left-arrow:horizontal, QScrollBar::right-arrow:horizontal {
                width: 26px;
                height: 26px;
                background: none;
            }
                        

        ''')
    
        self.table.setShowGrid(False);

        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(True)

        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(self.table, 0, 0, 0, 0)