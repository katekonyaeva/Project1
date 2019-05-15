from PyQt5 import QtWidgets
from design.index import Ui_MainWindow  # импорт нашего сгенерированного файла
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
 
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initUI()
    

    def initUI(self):
   
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        openFile = QAction(QIcon('open.png'), '&Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open new File')
        openFile.triggered.connect(self.showDialog)

        clearFile = QAction(QIcon('open.png'), '&Clear', self)
        clearFile.setShortcut('Ctrl+O')
        clearFile.setStatusTip('Open new File')
        clearFile.triggered.connect(self.showDialog)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Файл')
        fileMenu.addAction(exitAction)
        fileMenu = menubar.addMenu('&Фильтрация')
        fileMenu.addAction(openFile)
        fileMenu.addAction(clearFile)

        self.statusBar().showMessage('Ready')
        self.setWindowTitle('MRT FILTER')
        self.show()

    def showDialog(self):
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 120, 97, 84))
        self.layoutWidget.setObjectName("layoutWidget")
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton.setObjectName("radioButton")

def main():
    app = QtWidgets.QApplication([])
    application = MainWindow()
    application.show()
    sys.exit(app.exec())

main()