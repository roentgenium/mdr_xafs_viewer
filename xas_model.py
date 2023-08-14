from typing import Union
from PySide6.QtCore import QAbstractListModel, QAbstractTableModel
from PySide6.QtCore import Qt, QItemSelection, QModelIndex

from xas_data import XasDatum


# class XasModel(QAbstractListModel):
class XasModel(QAbstractTableModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._names: list[str] = []
        self._xasdata: list[XasDatum] = []


    def add(self, data: XasDatum):
        self._xasdata.append(data)


    def data(self, index, role):
        if role == Qt.DisplayRole:
            # spectrum = self._xasdata[index.row()]
            # return spectrum.name
            # print(index.row(), index.column())
            return self._xasdata[index.row()].toList()[index.column()]
        
        return None


    def rowCount(self, parent):
        return len(self._xasdata)


    def columnCount(self, parent):
        return len(XasDatum.toHeaderList())

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole:
            pass
            # The QTableView wants a header text

        if orientation == Qt.Horizontal:
            # BE CAREFUL about IndexError
            return XasDatum.toHeaderList()[section]

        return ""  # There is no vertical header

    def get(self, index: QModelIndex):
        return self._xasdata[index.row()].toList()[1]

        # indexes = index.indexes()
        # for i in indexes:
        #     print(i)
        #     data = i.data()
        #     print(data)

    #     return "OK"
        # data = []
        # for i in index:
        #     data.append(self._xasdata[i])

        # return data
        # return self._xasdata[index.row()]
    



    # def plot_data(self, index):
    #     spectrum = self.XasData[index.row()]

