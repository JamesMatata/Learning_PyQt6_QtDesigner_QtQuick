from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
import sys
import pyqtgraph as pg
import numpy as np


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Updating PyQtGraph Graphs")
        self.setGeometry(100, 100, 700, 500)

        vbox = QVBoxLayout()
        
        self.pw = pg.PlotWidget()

        btn = QPushButton("Update")
        btn.clicked.connect(self.show_plot)

        x = np.random.normal(size=100)
        y = np.random.normal(size=100)

        self.pw.plot(x, y, clea=True)

        vbox.addWidget(self.pw)

        vbox.addWidget(btn)

        self.setLayout(vbox)

    def update(self):
        x = np.random.normal(size=100)
        y = np.random.normal(size=100)

        self.pw.plot(x, y, clea=True)

    def show_plot(self):
        self.timer = pg.QtCore.QTimer()
        self.timer.setSingleShot(False)

        self.timer.timeout.connect(self.update)
        self.timer.start(100)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())