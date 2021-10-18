from PyQt5.QtCore import QThread, pyqtSignal
import sys
from mongoDBThread import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import QGridLayout
from communicationThread import *
from mainWindowUI import *


class MplCanvas(FigureCanvas):
    def __init__(self, width=5, height=4, dpi=100):
        figure = Figure(figsize=(width, height), dpi=dpi,  tight_layout=3.0)

        self.axes = figure.add_subplot(111)

        self.axes.set_title('CO2')

        self.axes.set_ylabel('ug/cm3', fontsize=15)

        super().__init__(figure)


class MyGraphThread(QThread):
    def __init__(self, tabPlot):
        super().__init__()
        self.canvas = MplCanvas()
        self.mpl = QGridLayout()
        self.mpl.addWidget(self.canvas)
        tabPlot.setLayout(self.mpl)

        self.ydata = [None]*10

        self.xdata = list(range(10))

    def run(self):

        while(1):
            time.sleep(10)

    def up_graph(self, data):

        try:

            self.ydata = self.ydata[1:]
            self.ydata.append(float(data[0]))

            print(self.ydata)
            print(self.xdata)
        except:
            self.ydata.append(None)
            print('Problem u konverziji!')

        # Nivo CO2
        self.canvas.axes.cla()  # cla funkija koja brise sve podatke sa grafika
        # sta hocemo da iscrtamo
        self.canvas.axes.plot(self.xdata, self.ydata, 'r')

        self.canvas.axes.set_title('Level of CO2')
        self.canvas.axes.set_ylabel('ug/cm3', fontsize=15)
        self.canvas.draw()  # iscrtavanje

    def exit(self):
        self.terminate()
