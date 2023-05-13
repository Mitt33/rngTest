from PyQt5.QtWidgets import QPushButton, QWidget, QLabel, QCheckBox, QGridLayout
from PyQt5.uic import loadUi
from gui.results import Results
from source import test_data, file_reader
from source.create_battery_of_tests import tooltip_dict


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

        self.back_btn = self.findChild(QPushButton, "btn_uncheck")
        self.back_btn.clicked.connect(self.uncheck_all)

        self.back_btn = self.findChild(QPushButton, "btn_check")
        self.back_btn.clicked.connect(self.check_all)

        self.grid_layout = self.findChild(QGridLayout, "gridLayout")

        self.head_label = self.findChild(QLabel, "label")

        self.file_path = file_path  # store file path in class variable
        self.binary_sequence = file_reader.file_read_prep(self.file_path)
        print(self.binary_sequence)
        print(self.binary_sequence.size)

        self.all_test_dict, self.eligible_battery = test_data.test_prep(self.binary_sequence)

        self.head_label.setText(
            "{} out of {} tests eligible (for sequence of {:,} inserted bits):".format(
                len(self.eligible_battery),
                len(self.all_test_dict),
                len(self.binary_sequence)))
        self.head_label.adjustSize()

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

            tooltip_text = tooltip_dict.get(test_name)
            if tooltip_text:
                checkbox.setToolTip(tooltip_text)

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
        screen_results = Results(self.widget, self.eligible_battery, self.main_window, self.binary_sequence)
        self.widget.addWidget(screen_results)
        self.widget.setCurrentWidget(screen_results)


    def check_all(self):
        for test_name, checkbox in self.checkboxes.items():
            if checkbox.isEnabled():  # check only eligible checkboxes
                checkbox.setChecked(True)

    def uncheck_all(self):
        for checkbox in self.checkboxes.values():
            checkbox.setChecked(False)
