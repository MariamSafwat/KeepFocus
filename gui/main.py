import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets 
from MyTab import MyTabWidget

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

        
class ProxyStyle(QtWidgets.QProxyStyle):
    def drawControl(self, element, opt, painter, widget):
        if element == QtWidgets.QStyle.CE_TabBarTabLabel:
            ic = self.pixelMetric(QtWidgets.QStyle.PM_TabBarIconSize)
            r = QtCore.QRect(opt.rect)
            w =  0 if opt.icon.isNull() else opt.rect.width() + self.pixelMetric(QtWidgets.QStyle.PM_TabBarIconSize)
            r.setHeight(opt.fontMetrics.width(opt.text) + w)
            r.moveBottom(opt.rect.bottom())
            opt.rect = r
        QtWidgets.QProxyStyle.drawControl(self, element, opt, painter, widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    QtWidgets.QApplication.setStyle(ProxyStyle())
    ex = App()
    sys.exit(app.exec_())
