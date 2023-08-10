from typing import Any
from PySide6.QtCore import QAbstractListModel, QModelIndex, QPersistentModelIndex
from PySide6.QtCore import Qt

from fileio import XasDatum

class XasModel(QAbstractListModel):
    def __init__(self, dat: XasDatum, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.XasData = dat or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            spectrum = self.XasData[index.row()]
            return spectrum.name
        # return super().data(index, role)

    def rowCount(self, parent):
        return len(self.XasData)
        # return super().rowCount(parent)
