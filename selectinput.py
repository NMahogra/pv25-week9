# selectinput.py

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Select Input")
        MainWindow.resize(400, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)

        self.label = QtWidgets.QLabel("Select an option:", self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 40, 120, 20))

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(160, 40, 150, 22))
        self.comboBox.addItems(["C", "C++", "Python"])

        self.pushButton = QtWidgets.QPushButton("OK", self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 100, 60, 30))

        self.pushButton_2 = QtWidgets.QPushButton("Cancel", self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 100, 60, 30))

        MainWindow.setCentralWidget(self.centralwidget)
