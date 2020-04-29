
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
                   
        # hold current table index    
        self.cur_table = 0
        
        # count no of lists changed 
        self.l_cnt = 0

        # Table Header
        self.table.setHorizontalHeaderLabels(
            'Activity|Catogery|Productivity'.split('|')) 
        self.table.horizontalHeader().setFixedHeight(50)
        
        # Disable columns resizing
        self.table.horizontalHeader().setSectionResizeMode (QHeaderView.Fixed);
        # Disable editing 
        self.table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

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
        
        ## Add Next, Prev, Save buttons
        # Next button
        self.nextButton = QPushButton('Next',self)
        self.nextButton.setStyleSheet("""
            QPushButton
            {
                height:30px;
                font-size:17px;
            }
            QPushButton:hover
            {
                background-color:#148CD2;
                border:none;
            }
            """)
        self.nextButton.setFixedWidth(200)
        self.nextButton.clicked.connect(self.nextContent)


        # Prev button 
        self.prevButton = QPushButton('Prev',self)
        self.prevButton.setStyleSheet("""
            QPushButton
            {
                height:30px;
                font-size:17px;
            }
            QPushButton:hover
            {
                background-color:#148CD2;
                border:none;
            }
            """)
        self.prevButton.setFixedWidth(200)
        self.prevButton.setDisabled(True)
        self.prevButton.clicked.connect(self.prevContent)
        
        # Save button 
        self.saveButton = QPushButton('Save',self)
        self.saveButton.setStyleSheet("""
            QPushButton
            {
                height:30px;
                font-size:18px;
            }
            QPushButton:hover
            {
                background-color:#148CD2;
                border:none;
            }
            """)
        self.saveButton.setDisabled(True)
        self.saveButton.clicked.connect(self.save)

        layout = QVBoxLayout (self)
        layout.addWidget(self.table)
        
        layout.setContentsMargins(20,30,20,30)
        buttons = QHBoxLayout(self)

        #buttons.setSpacing (700)
        buttons.setContentsMargins(0,0,25,80)
        buttons.addWidget(self.prevButton)
        buttons.addWidget(self.saveButton)
        buttons.addWidget(self.nextButton)
        layout.addLayout(buttons)


    def displayContent(self):

        self.table.clearContents()
        temp_database = self.temp_database[self.table.rowCount() * self.cur_table:]

        prod_list = []

        for row in range(self.table.rowCount()):
            
            if row >= len(temp_database):
                self.nextButton.setDisabled(True)
                return 

            for col in range(self.table.columnCount()):                     

                if col == 2:
                    prod_list.append(QComboBox())
                    # Fill in productivity list
                    for key , value in returnAllprogramStatus().items():
                        prod_list[row].addItem(value)
                    
                    prod_list[row].setStyleSheet("""
                        QComboBox{
                            border:none;
                            background-color:transparent;
                        }
                        QComboBox:selected{
                            background-color:#148CD2;
                        }
                    """)
                    # set default item to the item saved in database
                    prod_list[row].setCurrentIndex(temp_database[row][col])

                    # Connect list change to boxChange signal that enables saveButton 
                    prod_list[row].currentIndexChanged.connect(
                        lambda row, combobox=prod_list[row]: self.boxChange(row, combobox) 
                    )

                    self.table.setCellWidget(row, col, prod_list[row])

                else: 
                      
                    item = QtWidgets.QTableWidgetItem('{}'.format(temp_database[row][col]))
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    self.table.setItem(row, col, item)
                
                self.table.setRowHeight(row,50)    


    def nextContent(self):
        self.l_cnt = 0
        self.saveButton.setEnabled(False)

        self.cur_table += 1

        if (self.cur_table+1) * self.table.rowCount() == len(self.temp_database) : 
            self.nextButton.setDisabled(True)

        self.displayContent()
        self.prevButton.setDisabled(False)
        return
    

    def prevContent(self):
        self.l_cnt = 0
        self.saveButton.setEnabled(False)

        self.cur_table -= 1

        if (self.cur_table+1) * self.table.rowCount() == self.table.rowCount() :
            self.prevButton.setDisabled(True)
        
        self.displayContent()
        self.nextButton.setDisabled(False)
        return
                

    def boxChange(self,row, combobox):
        curIndex = combobox.currentIndex()
        print(row,curIndex)

        if self.temp_database[row][2] == curIndex:
            self.l_cnt -= 1
            if self.l_cnt == 0:
                self.saveButton.setDisabled(True)
        else:
            self.l_cnt += 1
            if self.l_cnt > 0:
                self.saveButton.setDisabled(False)
    
    def save(self):
        self.l_cnt = 0
        self.saveButton.setDisabled(True)