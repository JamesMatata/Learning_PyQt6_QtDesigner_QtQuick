from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLineEdit, QListWidget
import sys
import pyqtgraph as pg
import numpy as np

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQtGraph Bar Graph")
        self.setGeometry(100, 100, 800, 600)

        hbox = QHBoxLayout()

        win = pg.PlotWidget()

        x = np.arange(10)
        y1 = np.sin(x)
        y2 = 1.1 * np.sin(x + 1)
        y3 = 1.2 * np.sin(x + 2)

        bg1 = pg.BarGraphItem(x=x, height=y1, width=0.3, brush='r')

        bg2 = pg.BarGraphItem(x=x + 0.33, height=y2, width=0.3, brush='g')

        bg3 = pg.BarGraphItem(x=x + 0.66, height=y3, width=0.3, brush='b')

        win.addItem(bg1)
        win.addItem(bg2)
        win.addItem(bg3)

        hbox.addWidget(win)

        self.setLayout(hbox)

        
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
    