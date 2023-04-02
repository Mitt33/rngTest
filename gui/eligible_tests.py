from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QVBoxLayout, QLabel, QCheckBox, QGridLayout
from PyQt5.uic import loadUi

from gui.results import Results
from source import test_data, file_reader


class EligibleTests(QWidget):
    def __init__(self, file_path, widget, main_window):
        super(EligibleTests, self).__init__()
        loadUi("gui/ui/EligibleTests.ui", self)
        self.widget = widget
        self.main_window = main_window

        self.back_btn = self.findChild(QPushButton, "home_btn")
        self.back_btn.clicked.connect(self.go_to_main)

        self.test_btn = self.findChild(QPushButton, "pushButton")
        self.test_btn.clicked.connect(self.test)

        self.grid_layout = self.findChild(QGridLayout, "gridLayout")

        self.head_label = self.findChild(QLabel, "label")

        self.file_path = file_path  # store file path in class variable
        self.binary_sequence = file_reader.file_read_prep(self.file_path)
        print(self.binary_sequence)
        print(self.binary_sequence.size)

        self.all_test_dict, self.eligible_battery = test_data.test_prep(self.binary_sequence)

        self.head_label.setText(str(len(self.eligible_battery)) + " out of " + str(len(self.all_test_dict)) +
                                " tests eligible: ")

        num_cols = 3
        row = 0
        column = 0
        self.checkboxes = {}
        for test_name in self.all_test_dict:
            # Determine whether the test is eligible or not
            eligible = test_name in self.eligible_battery

            # Disable the checkbox if the test is not eligible
            disabled = not eligible

            # Create the checkbox
            checkbox = QCheckBox(test_name)
            checkbox.setChecked(eligible)
            checkbox.setDisabled(disabled)
            # checkbox.stateChanged.connect(self.test)

            self.checkboxes[test_name] = checkbox

            # Add the checkbox to the layout
            self.grid_layout.addWidget(checkbox, row, column)

            column += 1
            if column == num_cols:
                column = 0
                row += 1


    def go_to_main(self):
        # main_window = MainWindow(self.widget)
        # widget.removeWidget()
        self.widget.addWidget(self.main_window)
        self.widget.setCurrentWidget(self.main_window)

    def test(self):
        # Loop through the checkboxes and update the eligible_tests dictionary
        for test_name in self.checkboxes:
            checkbox = self.checkboxes[test_name]
            if checkbox.isEnabled() and checkbox.isChecked():
                self.eligible_battery[test_name] = self.all_test_dict[test_name]
            elif test_name in self.eligible_battery:
                del self.eligible_battery[test_name]

        print("test function activated")
        for name in self.eligible_battery.keys():
            print("-" + name)

        screen_results = Results(self.widget, self.eligible_battery, self.main_window, self.binary_sequence)
        self.widget.addWidget(screen_results)
        self.widget.setCurrentWidget(screen_results)

    def update_eligible_tests(self):
        # Loop through the checkboxes and update the eligible_tests dictionary
        pass

