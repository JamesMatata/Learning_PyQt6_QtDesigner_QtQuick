from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout
import sys
import pyqtgraph as pg
import numpy as np


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQtGraph Graph Legends")
        self.setGeometry(100, 100, 700, 500)

        my_plot = pg.PlotWidget()

        my_plot.addLegend()

        my_plot.plot([2,3,5,6,7,8], pen='g', fillLevel=0, fillBrush=(255,255,255, 30), name='Green Plot', )
        my_plot.plot([1,2,4,5,6,7], pen='r', name='Red Plot')
        my_plot.addLine(y=4, pen='b', name='Blue Line')

        hbox = QHBoxLayout()
        hbox.addWidget(my_plot)

        self.setLayout(hbox)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())