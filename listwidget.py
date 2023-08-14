from PySide6 import QtWidgets

class ListWidget(QtWidgets.QListView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMaximumSize(200, 800)
        self.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)

    def set_model(self, m):
        self.setModel(m)

