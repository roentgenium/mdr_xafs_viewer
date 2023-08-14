from xas_model import XasModel

from PySide6 import QtCore, QtWidgets

from plotwidget import PlotWidget
from controlwidget import ControlWidget
from listwidget import ListWidget

from xas_model import XasModel
from xas_data import XasDatum


class MdrXasViewer(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MdrXasViewer, self).__init__(parent)
        self.setWindowTitle("MDR XAFS Viewer")

        self.plotwidget = PlotWidget(self)
        self.controlwidget = ControlWidget(self)
        self.listwidget = ListWidget(self)

        self.widget = QtWidgets.QWidget()
        self.layout = QtWidgets.QGridLayout(self.widget)

        self.layout.addWidget(self.controlwidget, 0, 0)
        self.layout.addWidget(self.listwidget, 1, 0)
        self.layout.addWidget(self.plotwidget, 0, 1, 2, 1)

        self.menuBar = QtWidgets.QMenuBar(self)
        self.menuBar.addMenu("&File")
        self.menuBar.addMenu("&About")
        self.setMenuBar(self.menuBar)

        # exit_action = QAction("Exit", self)
        # exit_action.setShortcut("Ctrl+Q")
        # exit_action.triggered.connect(self.exit_app)
        # self.file_menu.addAction(exit_action)

        self.statusBar = QtWidgets.QStatusBar(self)
        self.setStatusBar(self.statusBar)

        self.statusBar.showMessage("Launched!")

        self.setCentralWidget(self.widget)

        self.model = XasModel()

    def set_model(self, m):
        self.model = m
        self.listwidget.set_model(m)
        # self.listwidget.selectionModel().currentChanged.connect(self.replot)
        self.listwidget.selectionModel().selectionChanged.connect(self.replot)

    def replot(self, selected, deselected):
        indexes = self.listwidget.selectedIndexes()
        data = []

        for i in indexes:
            data.append(self.model.get(i))
        for d in data:
            self.plotwidget.add_series(d)




    # @Slot()
    # def exit_app(self, checked):
    #     QApplication.quit()

    # @Slot()
    # def update_graph(self, selected, deselected):
    #     self.plot_widget.update_graph(self.xaslist_view.currentIndex())
    #     print(selected)

        ### Qt Signal/Slots
        # self.xaslist_view.selectionModel().selectionChanged.connect(self.update_graph)


        # self.s.update_timer.timeout.connect( self.updateStatusBar )
        # self.s.requestStatusUpdate.connect( self.sendRequestToMadoca )

        # self.gc.requestPurgeMadoca.connect( self.sendRequestToMadoca )

        # self.c.loadCondition.connect( self.setCondition )
        # self.c.saveCondition.connect( self.gatherCondition )
        
        # self.c.startMeasurement.connect( self.startMeasurement )
        # self.c.stopMeasurement.connect( self.finishMeasurement )
        # self.c.skipStep.connect( self.skipStep )
        # self.c.holdStep.connect( self.holdStep )

        # self.mainTimer.timeout.connect( self.moveNextStep )
        # self.qxafsTimer.timeout.connect( self.triggerQXAFS )
        # self.qxafsStopTimer.timeout.connect( self.qxafsStopTimer.stop )
        # self.qxafsStopTimer.timeout.connect( self.qxafsTimer.stop )

    def updateStatusBar(self):
        pass
