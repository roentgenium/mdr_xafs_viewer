import sys, glob, os
import matplotlib.pyplot as plt

from PySide6.QtWidgets import QApplication
from fileio import XasDatum

from XasModel import XasModel

from ui.main_window import MainWindow
from ui.main_widget import PlotWidget

def load_mdr_xafs(dir_name) -> list:

    # Make filename list of zip files in dir_name
    l = glob.glob(dir_name + "/*.zip")

    # Make XasDatum list
    data = []

    for z in l:
        data.append(XasDatum(z))

    return data


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Load MDR XAS data
    os.chdir("data")
    data = load_mdr_xafs(".")

    # Link data to XasModel
    XasListModel = XasModel(data)

    # XasListView = QListView()
    # XasListView.setModel(XasListModel)
    
    # plot_widget = PlotWidget(data[1])

    # main_window = MainWindow(plot_widget)
    main_window = MainWindow(XasListModel)
    main_window.resize(800, 600)
    main_window.show()

    sys.exit(app.exec())
