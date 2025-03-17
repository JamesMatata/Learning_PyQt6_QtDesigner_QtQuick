from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QListWidget
import sys
import pyqtgraph as pg
import numpy as np

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQtGraph Line Graph")
        self.setGeometry(100, 100, 800, 600)

        btn = QPushButton("Click Me")
        text = QLineEdit("Some Text")
        list = QListWidget()


        grid_layout = QGridLayout()

        plot = pg.PlotWidget()

        x = np.array([0, 5, 2, 8, 4])
        y = np.array([5, 6, 7, 8, 9])

        plot.plot(x, y)

        grid_layout.addWidget(btn, 0, 0)
        grid_layout.addWidget(text, 1, 0)
        grid_layout.addWidget(list, 2, 0)
        grid_layout.addWidget(plot, 0, 1, 3, 1)

        self.setLayout(grid_layout)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
    