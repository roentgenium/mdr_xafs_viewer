from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QListView, QWidget, QSizePolicy
from PySide6.QtGui import QAction
from PySide6.QtCore import Slot

from .main_widget import PlotWidget

class MainWindow(QMainWindow):
    def __init__(self, listmodel):
        QMainWindow.__init__(self)
        self.setWindowTitle("MDR XAFS Viewer")

        layout = QHBoxLayout()

        XasListView = QListView()
        XasListView.setModel(listmodel)
        XasListView.setMaximumSize(100, 800)

        plot_widget = PlotWidget()

        XasListView.selectionModel().selectionChanged.connect(plot_widget.update_graph)

        layout.addWidget(XasListView)
        layout.addWidget(plot_widget)

        widget = QWidget()
        widget.setLayout(layout)

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