from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QMainWindow, QPushButton, QMessageBox
from PyQt5.uic import loadUi

from gui.generate_numbers import GenerateNumbers
from gui.choose_file import ChooseFile


class MainWindow(QMainWindow):
    def __init__(self, widget):
        super(MainWindow, self).__init__()
        loadUi("gui/ui/MainWindow.ui", self)
        self.widget = widget

        self.generate_btn = self.findChild(QPushButton, "generate_btn")
        self.generate_btn.clicked.connect(self.go_to_generate)

        self.choose_btn = self.findChild(QPushButton, "choose_btn")
        self.choose_btn.clicked.connect(self.go_to_choose_file)

    def go_to_generate(self):
        try:
            screen_generate = GenerateNumbers(self.widget, self)
            self.widget.addWidget(screen_generate)
            self.widget.removeWidget(self)
            self.widget.setCurrentWidget(screen_generate)
        except Exception as e:
            # Create a message box to show the error information
            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Critical)
            error_box.setText("An error occurred: " + str(e))
            error_box.setWindowTitle("Error")
            error_box.exec_()

    def go_to_choose_file(self):
        try:
            screen_choose = ChooseFile(self.widget, self)
            self.widget.addWidget(screen_choose)
            self.widget.removeWidget(self)
            self.widget.setCurrentWidget(screen_choose)
        except Exception as e:
            # Create a message box to show the error information
            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Critical)
            error_box.setText("An error occurred: " + str(e))
            error_box.setWindowTitle("Error")
            error_box.exec_()
