import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, QDialog, QVBoxLayout, QLabel, QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets 
from gui.MyTab import MyTabWidget
from gui.firstTimeTut import Tutorial
from database.modelsfun import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'KeepFocus'
        self.setWindowTitle(self.title)
        
        show = ShowTutorial()
        if show is True:
            self.ft = Tutorial()
            self.ft.show()
        
            
        self.tab_widget = MyTabWidget(self)
        self.setCentralWidget(self.tab_widget)

        # add menu bar
        mainMenu = self.menuBar()
        mainMenu.setStyleSheet("color:#017ffc;padding:5px;")
        fileMenu = mainMenu.addMenu('File')

        # exit button
        exitButton = QAction('Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.setStatusTip('Exit application')
        exitButton.triggered.connect(self.quit)
        # About button
        aboutButton = QAction('About', self)
        aboutButton.setShortcut('Ctrl+B')
        aboutButton.setStatusTip('About application')
        aboutButton.triggered.connect(self.about)

        fileMenu.addAction(aboutButton)
        fileMenu.addAction(exitButton)

        self.showMaximized()
        self.setMinimumSize(700,650)
        self.setContentsMargins(0, 0, 0, 0);
        self.setStyleSheet("background-color:#22282d;")


    def about(self):
        aboutDialog = QDialog(self)
        aboutDialog.setFixedSize(400,200)
        aboutDialog.setWindowTitle("About")
        aboutDialog.setStyleSheet("background:white")

        layout = QVBoxLayout(self)
        label = QLabel(self)
        label.setText(
"""KeepFocus keeps tracking your screen, analyzing what \nyou are doing and giving you feedback on how to do\nbetter and how to be more productive.\n
It does so by taking a screenshot of the screen every\nfixed interval and using image processing technology to\nknow what you are doing and notify you when you lose\ntrack.\n\nCopyright © 2020 all rights reserved for TimeWorries
"""
        )
        layout.addWidget(label);
        aboutDialog.setLayout(layout);
        aboutDialog.show()        



    def init_tray(self):

        icon = QIcon("keepfocus_icon.png")
        self._tray = QSystemTrayIcon()
        self._tray.setIcon(icon)
        self._tray.setVisible(True)

        self._menu = QMenu()
        self._action = QAction("Hide")
        self._action.triggered.connect(self.hideit)
        
        self.quit_action = QAction("Quit")
        self.quit_action.triggered.connect(self.quit)

        self._menu.addAction(self._action)
        self._menu.addAction(self.quit_action)

        self._tray.setContextMenu(self._menu)


    def hideit(self):
        self.setVisible(False)
        self._action = QAction("Show")
        self._action.triggered.connect(self.Showit)

        self.quit_action = QAction("Quit")
        self.quit_action.triggered.connect(self.quit)

        self._menu.clear()
        self._menu.addAction(self._action)
        self._menu.addAction(self.quit_action)

        self._tray.setContextMenu(self._menu)



    def Showit(self):
        self.setVisible(True)
        self._action = QAction("Hide")
        self._action.triggered.connect(self.hideit)
        self._menu.clear()

        self.quit_action = QAction("Quit")
        self.quit_action.triggered.connect(self.quit)


        self._menu.addAction(self._action)
        self._menu.addAction(self.quit_action)

        self._tray.setContextMenu(self._menu)

    def closeEvent(self, event):
        event.ignore()
        self.hideit()

    def quit(self):
        app.quit()


if __name__ == '__main__':
    checkDay()
    QApplication.setStyle("Fusion")
    app = QApplication(sys.argv)

    def strt():
        splash.close()
        ex = App()
        ex.init_tray()
        sys.exit(app.exec_())

    splash_pix = QtGui.QPixmap('logo.jpg')
    splash_pix1 = splash_pix.scaled(550, 550, QtCore.Qt.KeepAspectRatio)
    splash = QSplashScreen(splash_pix1, QtCore.Qt.WindowStaysOnTopHint)
    splash.show()

    QtCore.QTimer.singleShot(3000, strt)
