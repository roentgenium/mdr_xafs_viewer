from PySide6 import QtWidgets, QtGui

from mainwindow import MdrXasViewer

from xas_data import XasDatum
from xas_model import XasModel

import os, glob

def load_mdr_xafs(dir_name) -> list:
    l = glob.glob(dir_name + "/*.zip")
    data = []

    for z in l:
        data.append(XasDatum(z))

    return data

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    os.chdir("data")
    data = load_mdr_xafs(".")

    m = XasModel()

    for d in data:
        m.add(d)

    mw = MdrXasViewer()
    mw.setFont(QtGui.QFont("Arial"))
    mw.resize(800, 600)
    mw.set_model(m)
    mw.show()

    sys.exit(app.exec())
