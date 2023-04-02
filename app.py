import sys

from PyQt5.QtWidgets import QMainWindow, \
    QApplication, QDialog, QStackedWidget, QLabel, QWidget, QPushButton

from gui.main_window import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    main_window = MainWindow(widget)
    widget.addWidget(main_window)
    widget.setFixedHeight(600)
    widget.setFixedWidth(800)
    widget.show()

    try:
        sys.exit(app.exec_())
    except:
        print("exiting")

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super(MainWindow, self).__init__()
#         loadUi("gui/ui/MainWindow.ui", self)
#
#         self.generate_btn = self.findChild(QPushButton, "generate_btn")
#         self.generate_btn.clicked.connect(self.go_to_generate)
#
#         self.choose_btn = self.findChild(QPushButton, "choose_btn")
#         self.choose_btn.clicked.connect(self.go_to_choose_file)
#
#     def go_to_generate(self):
#         screen_generate = GenerateNumbers()
#         widget.addWidget(screen_generate)
#         widget.removeWidget(main_window)
#         widget.setCurrentWidget(screen_generate)
#
#     def go_to_choose_file(self):
#         screen_choose = ChooseFile()
#         widget.addWidget(screen_choose)
#         widget.removeWidget(main_window)
#         widget.setCurrentWidget(screen_choose)


# class GenerateNumbers(QWidget):
#     def __init__(self):
#         super(GenerateNumbers, self).__init__()
#         loadUi("gui/ui/GenerateNumbers.ui", self)
#
#         self.back_btn = self.findChild(QPushButton, "back_btn")
#         self.back_btn.clicked.connect(self.go_to_main)
#
#         self.next_btn = self.findChild(QPushButton, "next_btn")
#         self.next_btn.clicked.connect(self.go_to_eligible)
#
#         self.combo_box = self.findChild(QComboBox, "comboBox")
#
#         self.spin_box = self.findChild(QSpinBox, "spinBox")
#
#         self.bit_length = 0
#         self.generators = source.generators.generators_list
#
#         for rng_name in self.generators:
#             self.combo_box.addItem(rng_name)
#         self.file_path = ""
#
#     def go_to_main(self):
#         main_window = MainWindow()
#         widget.addWidget(main_window)
#         widget.setCurrentWidget(main_window)
#
#     def go_to_eligible(self):
#         selected_generator = self.combo_box.currentText()
#         num_bits = self.spin_box.value()
#
#         print(num_bits)
#         print(selected_generator)
#         self.file_path = source.generators.generators_setup(selected_generator, num_bits)
#         print(self.file_path)
#
#         screen_eligible = EligibleTests(self.file_path)
#         widget.addWidget(screen_eligible)
#         widget.setCurrentWidget(screen_eligible)


# class ChooseFile(QWidget):
#     def __init__(self):
#         super(ChooseFile, self).__init__()
#         loadUi("gui/ui/ChooseFile.ui", self)
#
#         self.back_btn = self.findChild(QPushButton, "back_btn")
#         self.back_btn.clicked.connect(self.go_to_main)
#
#         self.next_btn = self.findChild(QPushButton, "next_btn")
#         self.next_btn.clicked.connect(self.go_to_eligible)
#
#         self.filepath_label = self.findChild(QLabel, "filepath_label")
#
#         self.choose_btn = self.findChild(QPushButton, "choose_btn")
#         self.choose_btn.clicked.connect(self.browse_file)
#
#         self.file_path = ""  # initialize class variable to hold the file path
#
#     def go_to_main(self):
#         main_window = MainWindow()
#         widget.addWidget(main_window)
#         widget.setCurrentWidget(main_window)
#
#     def go_to_eligible(self):
#         screen_eligible = EligibleTests(self.file_path)
#         widget.addWidget(screen_eligible)
#         widget.setCurrentWidget(screen_eligible)
#
#     def browse_file(self):
#         filename, _ = QFileDialog.getOpenFileNames(self, "Open file", "./generated_data/",
#                                                    "All files (*);;Binary files (*.bin);;Text files (*.txt)")
#         if filename:
#             self.file_path = filename[0]
#             self.filepath_label.setText(self.file_path)
#             self.filepath_label.adjustSize()


# class EligibleTests(QWidget):
#     def __init__(self, file_path):
#         super(EligibleTests, self).__init__()
#         loadUi("gui/ui/EligibleTests.ui", self)
#
#         self.back_btn = self.findChild(QPushButton, "home_btn")
#         self.back_btn.clicked.connect(self.go_to_main)
#
#         self.test_btn = self.findChild(QPushButton, "pushButton")
#
#         self.file_path = file_path  # store file path in class variable
#         self.binary_sequence = source.file_reader.file_read_prep(self.file_path)
#         print(self.binary_sequence)
#         print(self.binary_sequence.size)
#         test_data.test_prep(self.binary_sequence)
#
#     def go_to_main(self):
#         main_window = MainWindow()
#         widget.addWidget(main_window)
#         # widget.removeWidget()
#         widget.setCurrentWidget(main_window)

# def start():
#     app = QApplication(sys.argv)
#     widget = QStackedWidget()
#     main_window = MainWindow()
#     widget.addWidget(main_window)
#     widget.setFixedHeight(600)
#     widget.setFixedWidth(800)
#     widget.show()
#
#     try:
#         sys.exit(app.exec_())
#     except:
#         print("exiting")



