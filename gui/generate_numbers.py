from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QComboBox, QSpinBox, QMessageBox
from PyQt5.uic import loadUi

from gui.eligible_tests import EligibleTests

from source import generators


class GenerateNumbers(QWidget):
    def __init__(self, widget, main_window):
        super(GenerateNumbers, self).__init__()
        loadUi("gui/ui/GenerateNumbers.ui", self)
        self.widget = widget
        self.main_window = main_window

        self.back_btn = self.findChild(QPushButton, "back_btn")
        self.back_btn.clicked.connect(self.go_to_main)

        self.next_btn = self.findChild(QPushButton, "next_btn")
        self.next_btn.clicked.connect(self.go_to_eligible)

        self.combo_box = self.findChild(QComboBox, "comboBox")

        self.spin_box = self.findChild(QSpinBox, "spinBox")

        self.bit_length = 0
        self.generators = generators.generators_list

        for rng_name in self.generators:
            self.combo_box.addItem(rng_name)
        self.file_path = ""

    def go_to_main(self):
        # main_window = MainWindow(self.widget)
        self.widget.addWidget(self.main_window)
        self.widget.removeWidget(self)
        self.widget.setCurrentWidget(self.main_window)

    def go_to_eligible(self):
        try:
            selected_generator = self.combo_box.currentText()
            num_bits = self.spin_box.value()

            print(num_bits)
            print(selected_generator)
            self.file_path = generators.generators_setup(selected_generator, num_bits)
            print(self.file_path)

            screen_eligible = EligibleTests(self.file_path, self.widget, self.main_window)
            self.widget.addWidget(screen_eligible)
            self.widget.setCurrentWidget(screen_eligible)
        except Exception as e:
            # Create a message box to show the error information
            error_box = QMessageBox()
            error_box.setIcon(QMessageBox.Critical)
            error_box.setText("An error with generating numbers occurred: " + str(e))
            error_box.setWindowTitle("Error")
            error_box.exec_()
