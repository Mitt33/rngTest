import sys

from PyQt5.QtWidgets import QMainWindow, \
    QApplication, QDialog, QStackedWidget, QLabel, QWidget, QPushButton

from gui.main_window import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    main_window = MainWindow(widget)
    widget.addWidget(main_window)
    # widget.setFixedHeight(600)
    # widget.setFixedWidth(800)
    widget.resize(800, 600)
    widget.show()

    try:
        sys.exit(app.exec_())
    except:
        print("exiting")

