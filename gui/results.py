import sys

from numpy import round
from PyQt5.QtWidgets import QMainWindow, QPushButton, QWidget, QComboBox, QSpinBox, QLabel, QTableWidget, \
    QTableWidgetItem, QHeaderView
from PyQt5.uic import loadUi

from source.test_data import test_data, print_results


class Results(QWidget):
    def __init__(self, widget, eligible_battery, main_window, binary_sequence):
        super(Results, self).__init__()
        loadUi("gui/ui/Results.ui", self)
        self.widget = widget
        self.eligible_battery = eligible_battery
        self.main_window = main_window
        self.binary_sequence = binary_sequence

        self.exit_btn = self.findChild(QPushButton, "exit_btn")
        self.exit_btn.clicked.connect(exit)

        self.table = self.findChild(QTableWidget, "tableWidget")

        results = test_data(binary_sequence, eligible_battery)

        self.table.setRowCount(len(results))
        for row, (result, elapsed_time) in enumerate(results):
            self.table.setItem(row, 0, QTableWidgetItem(result.name))
            self.table.setItem(row, 1, QTableWidgetItem(str(round(result.score, 3))))
            self.table.setItem(row, 2, QTableWidgetItem(str(elapsed_time) + " ms"))
            passed_item = QTableWidgetItem("Passed" if result.passed else "Failed")
            self.table.setItem(row, 3, passed_item)

        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def exit(self):
        sys.exit()
