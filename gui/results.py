import sys
import time

from PyQt5.QtCore import QThread, pyqtSignal, Qt
from numpy import round
from PyQt5.QtWidgets import QPushButton, QWidget, QLabel, QTableWidget, \
    QTableWidgetItem, QHeaderView, QMessageBox, QProgressDialog, QFileDialog
from PyQt5.uic import loadUi
from source.tests.graphical_test import graphical_test
from source.create_battery_of_tests import tooltip_dict

from source.test_data import test_data, save_results_csv, save_results_xlsx, \
    save_results_txt


class Results(QWidget):
    def __init__(self, widget, eligible_battery, main_window, binary_sequence):
        super(Results, self).__init__()
        self.results = None
        loadUi("gui/ui/Results.ui", self)
        self.widget = widget
        self.eligible_battery = eligible_battery
        self.main_window = main_window
        self.binary_sequence = binary_sequence
        self.tooltip_dict = tooltip_dict

        self.exit_btn = self.findChild(QPushButton, "exit_btn")
        self.exit_btn.clicked.connect(exit)

        self.graphical_btn = self.findChild(QPushButton, "graphical_btn")
        self.graphical_btn.clicked.connect(self.graphical_test)

        self.graphical_btn = self.findChild(QPushButton, "export_btn")
        self.graphical_btn.clicked.connect(self.export)

        self.table = self.findChild(QTableWidget, "tableWidget")

        self.time_label = self.findChild(QLabel, "time_label")

        self.results_thread = ResultsThread(self.binary_sequence, self.eligible_battery)
        self.results_thread.result_ready.connect(self.show_table)
        self.results_thread.elapsed_time_ready.connect(self.update_elapsed_time)
        self.results_thread.start()

        self.progress_dialog = QProgressDialog(self)
        self.progress_dialog.setWindowModality(Qt.WindowModal)
        self.progress_dialog.setWindowTitle("Computing tests")
        self.progress_dialog.setLabelText("Computing tests...")
        self.progress_dialog.setCancelButtonText(None)
        self.progress_dialog.setRange(0, 0)
        self.progress_dialog.show()

    def show_table(self, results):
        self.results = results
        self.table.setRowCount(len(results))
        for row, (result, elapsed_time) in enumerate(results):
            self.table.setItem(row, 0, QTableWidgetItem(result.name))
            self.table.setItem(row, 1, QTableWidgetItem(str(round(result.score, 3))))
            self.table.setItem(row, 2, QTableWidgetItem(str(elapsed_time) + " ms"))
            passed_item = QTableWidgetItem("Passed" if result.passed else "Failed")
            self.table.setItem(row, 3, passed_item)

            tooltip = self.tooltip_dict.get(result.name, "No description available.")
            for col in range(self.table.columnCount()):
                self.table.item(row, col).setToolTip(tooltip)

        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.progress_dialog.hide()

    def update_elapsed_time(self, elapsed_time):
        self.time_label.setText(f"Elapsed time: {round(elapsed_time, 3)} seconds")

    def exit(self):
        sys.exit()

    def graphical_test(self):
        if len(self.binary_sequence) <= 700000:
            graphical_test(self.binary_sequence)
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Sequence is too long!")
            msg.setText(f"The sequence has {len(self.binary_sequence)} bits, only sequence up to 700 000 bits"
                        f" are suitable for graphicall visualization")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()

    def export(self):
        options = QFileDialog.Options()
        default_filename = 'test_results/results_export.xlsx'
        options |= QFileDialog.DontUseNativeDialog | QFileDialog.DontConfirmOverwrite
        file_name, _ = QFileDialog.getSaveFileName(self, "Export Results", default_filename,
                                                   "CSV Files (*.csv);;Excel Files (*.xlsx);;Text Files (*.txt)",
                                                   options=options)

        if file_name:
            exported_file = None
            try:
                if file_name.endswith('.csv'):
                    exported_file = save_results_csv(self.results, file_name)

                elif file_name.endswith('.xlsx'):
                    exported_file = save_results_xlsx(self.results, file_name)

                elif file_name.endswith('.txt'):
                    exported_file = save_results_txt(self.results, file_name)

                if exported_file:
                    info_box = QMessageBox()
                    info_box.setIcon(QMessageBox.Information)
                    info_box.setText("Export successful! \nFilepath to result: " + exported_file)
                    info_box.setWindowTitle("Export")
                    info_box.exec_()

            except Exception as e:
                error_box = QMessageBox()
                error_box.setIcon(QMessageBox.Critical)
                error_box.setText("An error with export occured: " + str(e))
                error_box.setWindowTitle("Error")
                error_box.exec_()


class ResultsThread(QThread):
    result_ready = pyqtSignal(list)
    elapsed_time_ready = pyqtSignal(float)

    def __init__(self, binary_sequence, eligible_battery):
        super().__init__()
        self.binary_sequence = binary_sequence
        self.eligible_battery = eligible_battery

    def run(self):
        start_time = time.time()
        results = test_data(self.binary_sequence, self.eligible_battery)
        end_time = time.time()
        elapsed_time = (end_time - start_time)
        self.result_ready.emit(results)
        self.elapsed_time_ready.emit(elapsed_time)
