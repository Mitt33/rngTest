import sys
import traceback

from PyQt5.QtWidgets import QApplication, QStackedWidget
from gui.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()
    main_window = MainWindow(widget)
    widget.addWidget(main_window)
    widget.resize(1000, 700)
    widget.show()

    try:
        sys.exit(app.exec_())
    except Exception as e:
        print(f"Exception occurred: {e}")
        traceback.print_exc()
