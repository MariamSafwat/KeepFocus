
from PyQt5 import QtCore, QtGui, QtWidgets 
from PyQt5.QtWidgets import QWidget,QComboBox, QPushButton, QHeaderView, QVBoxLayout,QHBoxLayout
from database.modelsfun import *

class MyTableWidget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.table = QtWidgets.QTableWidget(5, 3, self)

        self.temp_database = []
        self.database = session.query(Programsdata).all()
        for i in self.database:
            prog_category = returnProgramsCategory(i.name)
            self.temp_database.append((i.name,prog_category,i.productive))
                   
            
        self.cur_table = 0
        
        self.table.setHorizontalHeaderLabels(
            'Activity|Catogery|Productivity'.split('|')) 
        self.table.horizontalHeader().setFixedHeight(50)
        
        # Disable columns resizing
        self.table.horizontalHeader().setSectionResizeMode (QHeaderView.Fixed);
        # Disable editing 
        #self.table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        self.table.setColumnWidth(0,300)   
        self.table.setColumnWidth(1,350)   
        self.table.setColumnWidth(2,350)   

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
        

        layout = QVBoxLayout (self)
        layout.addWidget(self.table)
        
        layout.setContentsMargins(20,30,20,30)
        buttons = QHBoxLayout(self)

        buttons.setSpacing (700)
        buttons.setContentsMargins(0,0,30,80)
        buttons.addWidget(self.prevButton)
        buttons.addWidget(self.nextButton)
        layout.addLayout(buttons)

        
    

    def displayContent(self):

        self.table.clearContents()
        temp_database = self.temp_database[self.table.rowCount() * self.cur_table:]

        for row in range(self.table.rowCount()):
            
            if row >= len(temp_database):
                self.nextButton.setDisabled(True)
                return 

            for col in range(self.table.columnCount()):                     

                if col == 2:
                    prod_list = QComboBox()
                    # Fill in productivity list
                    for key , value in returnAllprogramStatus().items():
                        prod_list.addItem(value)
                    
                    prod_list.setStyleSheet("""
                        QComboBox{
                            border:none;
                            background-color:transparent;
                        }
                        QComboBox:selected{
                            background-color:#148CD2;
                        }
                    """)
                    # set default item to the item saved in database
                    prod_list.setCurrentIndex(temp_database[row][col])
                    self.table.setCellWidget(row, col, prod_list)

                else: 
                      
                    item = QtWidgets.QTableWidgetItem('{}'.format(temp_database[row][col]))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setItem(row, col, item)
                
                self.table.setRowHeight(row,50)    


    def nextContent(self):
        self.cur_table += 1

        if (self.cur_table+1) * self.table.rowCount() == len(self.temp_database) : 
            self.nextButton.setDisabled(True)

        self.displayContent()
        self.prevButton.setDisabled(False)
        return
    

    def prevContent(self):
        self.cur_table -= 1

        if (self.cur_table+1) * self.table.rowCount() == self.table.rowCount() :
            self.prevButton.setDisabled(True)
        
        self.displayContent()
        self.nextButton.setDisabled(False)
        return
                
