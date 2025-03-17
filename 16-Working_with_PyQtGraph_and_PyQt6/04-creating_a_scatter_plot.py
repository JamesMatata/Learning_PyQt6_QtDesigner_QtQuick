from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
import sys
import pyqtgraph as pg
import numpy as np

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQtGraph Scatter Plot")
        self.setGeometry(100, 100, 700, 500)

        x = np.random.normal(size=1000)
        y = np.random.random(size=1000)

        self.pw = pg.PlotWidget()

        self.plot = self.pw.plot(x,y,pen=None, symbol='o', symbolBrush=('b'), symbolSize=5)

        self.plot_btn = QPushButton("Replot")
        self.plot_btn.setStyleSheet("background-color: blue;padding: 10px;font-weight: bold;font-size: 16px;border: none;border-radius: 2px;")
        self.plot_btn.clicked.connect(self.plot_scatter)

        vbox = QVBoxLayout()

        vbox.addWidget(self.pw)
        vbox.addWidget(self.plot_btn)

        self.setLayout(vbox)

    def plot_scatter(self):
        x = np.random.normal(size=1000)
        y = np.random.random(size=1000)

        self.plot.setData(x, y)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
    