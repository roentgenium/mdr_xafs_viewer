from PySide6 import QtCharts, QtWidgets, QtCore, QtGui

from xas_data import XasDatum

class PlotWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.chart = QtCharts.QChart()

        self.chart_view = QtCharts.QChartView(self.chart)
        self.chart_view.setRenderHint(QtGui.QPainter.Antialiasing)
        self.chart_view.setMouseTracking(True)
        self.chart_view.setInteractive(True)
        self.chart_view.setRubberBand(QtCharts.QChartView.RectangleRubberBand)

        self.main_layout = QtWidgets.QHBoxLayout()
        size = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)

        self.chart_view.setSizePolicy(size)
        self.main_layout.addWidget(self.chart_view)

        self.setLayout(self.main_layout)

        self.series = QtCharts.QLineSeries()

        self.axis_x = QtCharts.QValueAxis()
        self.axis_x.setTickCount(10)
        self.axis_x.setLabelFormat("%.1f")
        self.axis_x.setTitleText("Energy / eV")
        self.chart.addAxis(self.axis_x, QtCore.Qt.AlignBottom)

        self.axis_y = QtCharts.QValueAxis()
        self.axis_y.setTickCount(10)
        self.axis_y.setLabelFormat("%.2f")
        self.axis_y.setTitleText("Absorption (a.u.)")
        self.chart.addAxis(self.axis_y, QtCore.Qt.AlignLeft)

    def add_series(self, data: XasDatum):
        self.chart.removeAllSeries()

        self.series = QtCharts.QLineSeries()
        self.series.setName(data.name)

        for i in range(len(data.energy)):
            self.series.append(data.energy[i], data.mu[i])

        self.chart.addSeries(self.series)
        self.series.attachAxis(self.axis_x)
        self.series.attachAxis(self.axis_y)

        self.set_autoscale(data)

    def remove_series(self, data: XasDatum):
        pass


    def replot(self, data):
        pass

    def set_autoscale(self, data=None):
        self.axis_x.setMin(min(data.energy))
        self.axis_x.setMax(max(data.energy))
        self.axis_y.setMin(min(data.mu))
        self.axis_y.setMax(max(data.mu))

    def clear(self):
        self.chart.removeAxis()

