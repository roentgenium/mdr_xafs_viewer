from PySide6 import QtWidgets


class ControlWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.xanes_label = QtWidgets.QLabel("XANES")
        self.xanes_button = QtWidgets.QCheckBox()

        self.clear_button = QtWidgets.QPushButton("Clear")

        main_layout = QtWidgets.QGridLayout()

        main_layout.addWidget(self.xanes_label, 0, 0)
        main_layout.addWidget(self.xanes_button, 0, 1)
        main_layout.addWidget(self.clear_button, 1, 0, 1, 2)

        self.setLayout(main_layout)

        

