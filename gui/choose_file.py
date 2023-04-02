from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QLabel, QFileDialog
from PyQt5.uic import loadUi

from gui.eligible_tests import EligibleTests


class ChooseFile(QWidget):
    def __init__(self, widget, main_window):
        super(ChooseFile, self).__init__()
        loadUi("gui/ui/ChooseFile.ui", self)
        self.widget = widget
        self.main_window = main_window

        self.back_btn = self.findChild(QPushButton, "back_btn")
        self.back_btn.clicked.connect(self.go_to_main)

        self.next_btn = self.findChild(QPushButton, "next_btn")
        self.next_btn.clicked.connect(self.go_to_eligible)

        self.filepath_label = self.findChild(QLabel, "filepath_label")

        self.choose_btn = self.findChild(QPushButton, "choose_btn")
        self.choose_btn.clicked.connect(self.browse_file)

        self.file_path = ""  # initialize class variable to hold the file path

    def go_to_main(self):
        # main_window = MainWindow(self.widget)
        self.widget.addWidget(self.main_window)
        self.widget.setCurrentWidget(self.main_window)

    def go_to_eligible(self):
        screen_eligible = EligibleTests(self.file_path, self.widget, self.main_window)
        self.widget.addWidget(screen_eligible)
        self.widget.setCurrentWidget(screen_eligible)

    def browse_file(self):
        filename, _ = QFileDialog.getOpenFileNames(self, "Open file", "./generated_data/",
                                                   "All files (*);;Binary files (*.bin);;Text files (*.txt)")
        if filename:
            self.file_path = filename[0]
            self.filepath_label.setText(self.file_path)
            self.filepath_label.adjustSize()