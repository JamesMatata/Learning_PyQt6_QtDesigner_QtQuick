from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys

class window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(200,200, 700, 400)
        self.setWindowTitle("PyQt6 QGridLayout")
        self.setWindowIcon(QIcon('images/icon.png'))

        # Grid Layout is used to arrange widgets in a grid
        grid = QGridLayout()

        btn1 = QPushButton("Button 1")
        btn2 = QPushButton("Button 2")
        btn3 = QPushButton("Button 3")
        btn4 = QPushButton("Button 4")
        btn5 = QPushButton("Button 5")
        btn6 = QPushButton("Button 6")
        btn7 = QPushButton("Button 7")
        btn8 = QPushButton("Button 8")

        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 0, 1)
        grid.addWidget(btn3, 0, 2)
        grid.addWidget(btn4, 0, 3)
        grid.addWidget(btn5, 1, 0)
        grid.addWidget(btn6, 1, 1)
        grid.addWidget(btn7, 1, 2)
        grid.addWidget(btn8, 1, 3)

        self.setLayout(grid)



app = QApplication(sys.argv)
window = window()
window.show()
sys.exit(app.exec())