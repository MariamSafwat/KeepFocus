
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QWidget,QComboBox, QPushButton, QHeaderView

class MyTableWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.table = QtWidgets.QTableWidget(4, 3, self)

        self.temp_database = [
                            ('google-chrome','BROWSERS'),
                            ('facebook','SOCIAL MEDIA'),
                            ('whatsApp-web','SOCIAL MEDIA'),
                            ('instagram','SOCIAL MEDIA'),
                            ('tiktok','ENTERTAINMENT'),
                            ('code','SOFTWARE DEV'),
                            ('libreoffice-impress','PRESENTATION'),
                            ('acroread','GENERAL'),
                            ('gnome-terminal','GENERAL'),

                        ]
        self.cur_table = 0
        
        self.table.setHorizontalHeaderLabels(
            'Activity|Catogery|Productivity'.split('|')) 
        self.table.horizontalHeader().setFixedHeight(50)
        
        # Disable columns resizing
        self.table.horizontalHeader().setSectionResizeMode (QHeaderView.Fixed);
        # Disable editing 
        #self.table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

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
        self.displayContent()
        
        self.table.setShowGrid(False);
        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(True)
        
        ## Add Next, Prev buttons
        # Next button
        self.nextButton = QPushButton('Next',self)
        self.nextButton.setStyleSheet("""
            QPushButton
            {
                height:25px;
            }
            QPushButton:hover
            {
                background-color:#148CD2;
                border:none;
            }
            """)
        self.nextButton.clicked.connect(self.nextContent)


        # Prev button 
        self.prevButton = QPushButton('Prev',self)
        self.prevButton.setStyleSheet("""
            QPushButton
            {
                height:25px;
            }
            QPushButton:hover
            {
                background-color:#148CD2;
                border:none;
            }
            """)
        self.prevButton.setDisabled(True)
        self.prevButton.clicked.connect(self.prevContent)
        
        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(self.table, 0, 0, 0, 0)
        layout.addWidget(self.nextButton, 0,8,1,1)
        layout.addWidget(self.prevButton,0,0,1,1)


    def displayContent(self):
        self.table.clearContents()
        temp_database = self.temp_database[4*self.cur_table:]

        for row in range(self.table.rowCount()):
            
            if row >= len(temp_database):
                self.nextButton.setDisabled(True)
                return 

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

    def nextContent(self):
        self.cur_table += 1

        if (self.cur_table+1)*4 == len(self.temp_database) : 
            self.nextButton.setDisabled(True)

        self.displayContent()
        self.prevButton.setDisabled(False)
        return
    
    def prevContent(self):
        self.cur_table -= 1

        if (self.cur_table+1) * 4 == 4:
            self.prevButton.setDisabled(True)
        
        self.displayContent()
        self.nextButton.setDisabled(False)
        return
                