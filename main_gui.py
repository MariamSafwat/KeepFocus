import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets 
from gui.MyTab import MyTabWidget

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'KeepFocus'
        self.setWindowTitle(self.title)        
        self.tab_widget = MyTabWidget(self)
        self.setCentralWidget(self.tab_widget)
        self.showMaximized()
        self.setContentsMargins(0, 0, 0, 0);
        self.setStyleSheet("background-color:#22282d;")

        
if __name__ == '__main__':
        
    QApplication.setStyle("Fusion")
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
