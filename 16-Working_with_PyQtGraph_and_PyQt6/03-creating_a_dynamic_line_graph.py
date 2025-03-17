from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QListWidget
import sys
import pyqtgraph as pg
import numpy as np

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQtGraph Dynamic Line Graph")
        self.setGeometry(100, 100, 800, 600)

        hbox = QHBoxLayout()
        hbox2 = QHBoxLayout()
        hbox3 = QHBoxLayout()
        vbox = QVBoxLayout()

        self.x1 = QLineEdit()
        self.x1.setPlaceholderText("x1")
        self.x2 = QLineEdit()
        self.x2.setPlaceholderText("x2")
        self.x3 = QLineEdit()
        self.x3.setPlaceholderText("x3")
        self.x4 = QLineEdit()
        self.x4.setPlaceholderText("x4")

        self.y1 = QLineEdit()
        self.y1.setPlaceholderText("y1")
        self.y2 = QLineEdit()
        self.y2.setPlaceholderText("y2")
        self.y3 = QLineEdit()
        self.y3.setPlaceholderText("y3")
        self.y4 = QLineEdit()
        self.y4.setPlaceholderText("y4")

        btn = QPushButton("Plot")
        btn.clicked.connect(self.plot)

        btn2 = QPushButton("Clear")
        btn2.clicked.connect(self.clear)

        self.plot = pg.PlotWidget()

        hbox.addWidget(self.x1)
        hbox.addWidget(self.x2)
        hbox.addWidget(self.x3)
        hbox.addWidget(self.x4)

        hbox2.addWidget(self.y1)
        hbox2.addWidget(self.y2)
        hbox2.addWidget(self.y3)
        hbox2.addWidget(self.y4)

        hbox3.addWidget(btn)
        hbox3.addWidget(btn2)

        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)

        vbox.addWidget(self.plot)

        vbox.addLayout(hbox3)

        self.setLayout(vbox)

    def plot(self):
        x1 = int(self.x1.text())
        x2 = int(self.x2.text())
        x3 = int(self.x3.text())
        x4 = int(self.x4.text())

        y1 = int(self.y1.text())
        y2 = int(self.y2.text())
        y3 = int(self.y3.text())
        y4 = int(self.y4.text())

        if x1 and x2 and x3 and x4 and y1 and y2 and y3 and y4:
            x = np.array([x1, x2, x3, x4])
            y = np.array([y1, y2, y3, y4])

            self.plot.plot(x, y)
        else:
            return
        
    def clear(self):
        self.plot.clear()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
    