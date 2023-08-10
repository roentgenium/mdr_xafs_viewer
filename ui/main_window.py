from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QAction
from PySide6.QtCore import Slot

class MainWindow(QMainWindow):
    def __init__(self, widget):
        QMainWindow.__init__(self)
        self.setWindowTitle("MDR XAFS Viewer")
        self.setCentralWidget(widget)

        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)

        self.file_menu.addAction(exit_action)

    @Slot()
    def exit_app(self, checked):
        QApplication.quit()