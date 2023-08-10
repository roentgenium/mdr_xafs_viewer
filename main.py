import sys
import matplotlib.pyplot as plt

from PySide6.QtWidgets import QApplication

import fileio

from ui.main_window import MainWindow
from ui.main_widget import PlotWidget

from util.mdr_xafs_util import find_raw_data

if __name__ == "__main__":
    app = QApplication(sys.argv)

    spectrum = fileio.XasDatum()

    path = "util/"

    dname, fname = find_raw_data(path + "c247dv91k.zip")
    print(dname, fname)

    data = spectrum.from_file(path + dname + "/" + fname[0])
    # data = spectrum.from_file("Cu-K_Cu-foil_Si311_50ms_140625.dat")
    # data = spectrum.from_file("Pb-L21_PbTe_Si311_50ms_210210.dat")
    # data = spectrum.from_file("rTiO2_Ti-K.dat")

    plot_widget = PlotWidget(data)

    main_window = MainWindow(plot_widget)
    main_window.resize(800, 600)
    main_window.show()

    sys.exit(app.exec())
