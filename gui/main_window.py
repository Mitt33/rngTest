from PyQt5.QtWidgets import QMainWindow, QPushButton
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
        screen_generate = GenerateNumbers(self.widget, self)
        self.widget.addWidget(screen_generate)
        self.widget.removeWidget(self)
        self.widget.setCurrentWidget(screen_generate)

    def go_to_choose_file(self):
        screen_choose = ChooseFile(self.widget, self)
        self.widget.addWidget(screen_choose)
        self.widget.removeWidget(self)
        self.widget.setCurrentWidget(screen_choose)
