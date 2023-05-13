import os
from PyQt5.QtWidgets import QPushButton, QWidget, QLabel, QFileDialog, QMessageBox
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

        self.check_label = self.findChild(QLabel, "check_label")

        self.choose_btn = self.findChild(QPushButton, "choose_btn")
        self.choose_btn.clicked.connect(self.browse_file)

        self.choose_btn.setToolTip("<p>It is possible to insert <strong>.txt</strong> and <strong>.bin</strong> "
                                   "files containing <strong>bit</strong> values. In the case of a text file "
                                   "with numbers, they will "
                                   "be converted to bits assuming that they are uint8 numbers (larger ones will "
                                   "be truncated), numbers on the interval (0,1) are rounded to bits. Values can be "
                                   "separated by a <strong>newline</strong>, <strong>comma</strong>, "
                                   "or <strong>space</strong>.</p>")

        self.file_path = ""

    def go_to_main(self):
        self.widget.addWidget(self.main_window)
        self.widget.setCurrentWidget(self.main_window)

    def go_to_eligible(self):
        if not self.file_path:
            msg_box = QMessageBox()
            msg_box.setIcon(QMessageBox.Warning)
            msg_box.setWindowTitle("Warning")
            msg_box.setText("Please select a file path first.")
            msg_box.exec_()
            return
        screen_eligible = EligibleTests(self.file_path, self.widget, self.main_window)
        self.widget.addWidget(screen_eligible)
        self.widget.setCurrentWidget(screen_eligible)

    def browse_file(self):
        file_path, _ = QFileDialog.getOpenFileNames(self, "Open file", "./generated_data/",
                                                    "All files (*);;Binary files (*.bin);;Text files (*.txt)")
        if file_path:
            success_msg = "<b>File successfully selected!</b>"
            self.file_path = file_path[0]
            filename = os.path.basename(self.file_path)
            self.filepath_label.setText("<b>Selected file: </b>" + filename)
            self.check_label.setText(success_msg)
