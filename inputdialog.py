# inputdialog.py

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction
import sys
import integerinput
import selectinput
import textinput

class InputDialogWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Input Dialog Menu")
        self.setGeometry(100, 100, 600, 400)
        self.create_menu()
        self.child_window = None

    def create_menu(self):
        menubar = self.menuBar()
        input_menu = menubar.addMenu("Input Menu")

        integer_action = QAction("Integer Input", self)
        integer_action.triggered.connect(self.open_integer_input)
        input_menu.addAction(integer_action)

        select_action = QAction("Select Input", self)
        select_action.triggered.connect(self.open_select_input)
        input_menu.addAction(select_action)

        text_action = QAction("Text Input", self)
        text_action.triggered.connect(self.open_text_input)
        input_menu.addAction(text_action)

    def close_current_child(self):
        if self.child_window:
            self.child_window.close()
            self.child_window = None

    def open_integer_input(self):
        self.close_current_child()
        self.child_window = QtWidgets.QMainWindow()
        self.ui = integerinput.Ui_MainWindow()
        self.ui.setupUi(self.child_window)
        self.ui.pushButton_2.clicked.connect(self.child_window.close)
        self.child_window.show()

    def open_select_input(self):
        self.close_current_child()
        self.child_window = QtWidgets.QMainWindow()
        self.ui = selectinput.Ui_MainWindow()
        self.ui.setupUi(self.child_window)
        self.ui.pushButton_2.clicked.connect(self.child_window.close)
        self.child_window.show()

    def open_text_input(self):
        self.close_current_child()
        self.child_window = QtWidgets.QMainWindow()
        self.ui = textinput.Ui_MainWindow()
        self.ui.setupUi(self.child_window)
        self.ui.pushButton_2.clicked.connect(self.child_window.close)
        self.child_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = InputDialogWindow()
    mainWin.show()
    sys.exit(app.exec_())
